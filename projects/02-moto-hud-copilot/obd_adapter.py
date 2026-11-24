"""Read supported standard PIDs. TPMS availability varies by motorcycle."""
def read_standard(connection):
    try: import obd
    except ImportError as e: raise RuntimeError('Install the obd extra') from e
    out = {}
    for name, command, unit in [('coolant_c', obd.commands.COOLANT_TEMP, 'celsius'), ('voltage', obd.commands.CONTROL_MODULE_VOLTAGE, 'volt')]:
        response = connection.query(command)
        if response is not None and not response.is_null():
            out[name] = float(response.value.to(unit).magnitude)
    return out
