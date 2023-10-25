from magic_class import MagicClass
import dis

if __name__ == "__main__":
    # Disassemble MagicClass methods to compare with given bytecode
    print("Disassembly of __init__:")
    dis.dis(MagicClass.__init__)

    print("Disassembly of area:")
    dis.dis(MagicClass.area)

    print("Disassembly of circumference:")
    dis.dis(MagicClass.circumference)

    # Test MagicClass
    try:
        mc = MagicClass("test")
    except Exception as e:
        print("Exception:", e)

    mc = MagicClass(5)
    print("Area:", mc.area())
    print("Circumference:", mc.circumference())
