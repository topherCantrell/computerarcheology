import opcodetools.cpu.base_cpu


_CPUS = {}


def get_cpu_by_name(name: str) -> opcodetools.cpu.base_cpu.CPU:

    if name in _CPUS:
        return _CPUS[name]

    # Delayed imports ... only for the processors we need

    cp = None
    if name == '6502':
        import opcodetools.cpu.cpu_6502
        cp = opcodetools.cpu.cpu_6502.CPU_6502()
    elif name == '6803':
        import opcodetools.cpu.cpu_6803
        cp = opcodetools.cpu.cpu_6803.CPU_6803()
    elif name == '6809':
        import opcodetools.cpu.cpu_6809
        cp = opcodetools.cpu.cpu_6809.CPU_6809()
    elif name == '8052':
        import opcodetools.cpu.cpu_8052
        cp = opcodetools.cpu.cpu_8052.CPU_8052()
    elif name == 'DVG':
        import opcodetools.cpu.cpu_DVG
        cp = opcodetools.cpu.cpu_DVG.CPU_DVG()
    elif name == 'Z80':
        import opcodetools.cpu.cpu_Z80
        cp = opcodetools.cpu.cpu_Z80.CPU_Z80()
    elif name == 'Z80GB':
        import opcodetools.cpu.cpu_Z80GB
        cp = opcodetools.cpu.cpu_Z80GB.CPU_Z80GB()

    if cp:
        _CPUS[name] = cp

    return cp
