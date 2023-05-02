import platform
import linux_smart
import windows_defrag_analyzer

if __name__ == "__main__":
    if platform.system() == "Windows":
        windows_defrag_analyzer.main()
    elif platform.system() == "Linux":
        linux_smart.main()