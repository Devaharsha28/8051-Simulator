import json
from flask import Flask, make_response, render_template, request, jsonify
from core.controller import Controller
from core.util import fill_memory

CLEAR_TOKEN = "batman"
app = Flask(__name__, static_folder="static")
controller = Controller()

app.jinja_env.globals.update(zip=zip)

def _chunk_memory(mem_dict):
    if not mem_dict:
        return []
    items = list(mem_dict.items())
    # Sort by address
    items.sort(key=lambda x: int(str(x[0]), 16))
    return [items[idx : idx + 16] for idx in range(0, len(items), 16)]

def _get_ram_and_rom():
    mem_sorted = fill_memory(controller.op.memory_ram, 256).sort()
    ram_dict = {k: v for k, v in mem_sorted.items() if int(str(k), 16) < 0x80}
    sfr_dict = {k: v for k, v in mem_sorted.items() if int(str(k), 16) >= 0x80}

    _memory_ram = _chunk_memory(ram_dict)
    _memory_sfr = _chunk_memory(sfr_dict)

    _rom = fill_memory(controller.op.memory_rom, 256).sort()
    _memory_rom = _chunk_memory(_rom)

    return _memory_ram, _memory_rom, _memory_sfr

def get_full_state():
    ram, rom, sfr = _get_ram_and_rom()
    
    # Serialize memory chunks: list of lists of [addr, val]
    def serialize_chunks(chunks):
        if not chunks: return []
        return [ [[k, str(v)] for k, v in chunk] for chunk in chunks ]

    # Serialize GPR
    gpr = controller.op.super_memory._general_purpose_registers
    gpr_serialized = {}
    for bank, regs in gpr.items():
        gpr_serialized[bank] = {k: str(v) for k, v in regs.items()}

    return {
        "registers": controller.op.super_memory._registers_todict(),
        "flags": controller.op.super_memory.PSW.flags(),
        "general_purpose_registers": gpr_serialized,
        "ram": serialize_chunks(ram),
        "rom": serialize_chunks(rom),
        "sfr": serialize_chunks(sfr),
        "assembler": controller.op._assembler,
        "index": controller._run_idx,
        "ready": controller.ready
    }

@app.route("/reset", methods=["POST"])
def reset():
    global controller
    controller.reset()
    return jsonify(get_full_state())

@app.route("/assemble", methods=["POST"])
def assemble():
    global controller
    commands_json = request.data
    if commands_json:
        commands_dict = json.loads(commands_json)
        _commands = commands_dict.get("code", None)
        _flags = commands_dict.get("flags", None)
        
        if _flags:
             controller.set_flags(_flags)

        if _commands:
            try:
                controller.parse_all(_commands)
                return jsonify(get_full_state())
            except Exception as e:
                print(e)
                return make_response(jsonify({"error": f"Exception raised {e}"}), 400)
    return make_response("Record not found", 400)

@app.route("/run", methods=["POST"])
def run():
    global controller
    if controller.ready:
        try:
            controller.run()
            controller.inspect()
            return jsonify(get_full_state())
        except Exception as e:
            print(e)
            return make_response(jsonify({"error": f"Exception raised {e}"}), 400)
    return make_response("Controller not ready", 400)

@app.route("/run-once", methods=["POST"])
def step():
    global controller
    if controller.ready:
        try:
            controller.run_once()
            return jsonify(get_full_state())
        except Exception as e:
            print(e)
            return make_response(jsonify({"error": f"Exception raised {e}"}), 400)
    return make_response("Controller not ready", 400)

@app.route("/memory-edit", methods=["POST"])
def update_memory():
    global controller
    mem_data = request.data
    if mem_data:
        mem_data = json.loads(mem_data)
        try:
            for memloc, memdata in mem_data:
                controller.op.memory_ram.write(memloc, memdata)
            return jsonify(get_full_state())
        except Exception as e:
            print(e)
            return make_response(jsonify({"error": f"Exception raised {e}"}), 400)
    return make_response("Controller not ready", 400)

@app.route("/", methods=["GET"])
def main():
    global controller
    controller = Controller()
    return render_template("index.html")
