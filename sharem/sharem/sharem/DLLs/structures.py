from struct import pack, unpack
from time import gmtime, localtime
from ..helper.emuHelpers import Uc

class struct_PROCESSENTRY32:
    # Backs both PROCESSENTRY32 and PROCESSENTRY32W
    def __init__(self, processID, threadCount, parent_pID, baseThreadPriority, exeFile: str):
        self.dwSizeA = 296 # Ascii Size
        self.dwSizeW = 556 # Unicode Size
        self.cntUsage = 0 # No Longer Used
        self.th32ProcessID = processID
        self.th32DefaultHeapID = 0 # No Longer Used
        self.th32ModuleID = 0 # No Longer Used
        self.cntThreads= threadCount
        self.th32ParentProcessID = parent_pID
        self.pcPriClassBase = baseThreadPriority
        self.dwFlags = 0 # No Longer Used
        self.szExeFile = exeFile

    def writeToMemoryA(self, uc: Uc, address):
        packedStruct = pack('<IIILIIIlI260s', self.dwSizeA, self.cntUsage, self.th32ProcessID, self.th32DefaultHeapID, self.th32ModuleID, self.cntThreads, self.th32ParentProcessID, self.pcPriClassBase, self.dwFlags, self.szExeFile.encode('ascii'))
        uc.mem_write(address, packedStruct)

    def readFromMemoryA(self, uc: Uc, address):
        data = uc.mem_read(address, self.dwSizeA)
        unpackedStruct = unpack('<IIILIIIlI260s', data)
        self.dwSizeA = unpackedStruct[0]
        self.cntUsage = unpackedStruct[1]
        self.th32ProcessID = unpackedStruct[2]
        self.th32DefaultHeapID = unpackedStruct[3]
        self.th32ModuleID = unpackedStruct[4]
        self.cntThreads = unpackedStruct[5]
        self.th32ParentProcessID = unpackedStruct[6]
        self.pcPriClassBase = unpackedStruct[7]
        self.dwFlags = unpackedStruct[8]
        self.szExeFile = unpackedStruct[9].decode()

    def writeToMemoryW(self, uc: Uc, address):
        packedStruct = pack('<IIILIIIlI520s', self.dwSizeW, self.cntUsage, self.th32ProcessID, self.th32DefaultHeapID, self.th32ModuleID, self.cntThreads, self.th32ParentProcessID, self.pcPriClassBase, self.dwFlags,self.szExeFile.encode('utf-16')[2:])
        uc.mem_write(address, packedStruct)

    def readFromMemoryW(self, uc: Uc, address):
        data = uc.mem_read(address, self.dwSizeW)
        unpackedStruct = unpack('<IIILIIIlI520s', data)
        self.dwSizeW = unpackedStruct[0]
        self.cntUsage = unpackedStruct[1]
        self.th32ProcessID = unpackedStruct[2]
        self.th32DefaultHeapID = unpackedStruct[3]
        self.th32ModuleID = unpackedStruct[4]
        self.cntThreads = unpackedStruct[5]
        self.th32ParentProcessID = unpackedStruct[6]
        self.pcPriClassBase = unpackedStruct[7]
        self.dwFlags = unpackedStruct[8]
        self.szExeFile = unpackedStruct[9].decode()

class struct_THREADENTRY32:
    def __init__(self, ThreadID, OwnerProcessID, tpBasePri):
        self.dwSize = 28
        self.cntUsage = 0 # No Longer Used
        self.th32ThreadID = ThreadID
        self.th32OwnerProcessID = OwnerProcessID
        if tpBasePri < 0 or tpBasePri > 31: # Value 0 to 31
            tpBasePri = 16 # Set to Middle Priority
        self.tpBasePri = tpBasePri
        self.tpDeltaPri = 0 # No Longer Used
        self.dwFlags = 0 # No Longer Used

    def writeToMemory(self, uc: Uc, address):
        packedStruct = pack('<IIIIllI', self.dwSize, self.cntUsage, self.th32ThreadID, self.th32OwnerProcessID, self.tpBasePri, self.tpDeltaPri, self.dwFlags)
        uc.mem_write(address, packedStruct)

    def readFromMemory(self, uc: Uc, address):
        data = uc.mem_read(address, self.dwSize)
        unpackedStruct = unpack('<IIIIllI', data)
        self.dwSize = unpackedStruct[0]
        self.cntUsage = unpackedStruct[1]
        self.th32ThreadID = unpackedStruct[2]
        self.th32OwnerProcessID = unpackedStruct[3]
        self.tpBasePri = unpackedStruct[4]
        self.tpDeltaPri = unpackedStruct[5]
        self.dwFlags = unpackedStruct[6]

class struct_MODULEENTRY32:
    # Backs both MODULEENTRY32 and MODULEENTRY32W
    def __init__(self, th32ProcessID, modBaseAddr, modBaseSize, hModule, szModule: str, szExePath: str):
        self.dwSizeA = 548 # Ascii Size
        self.dwSizeW = 1064 # unicode Size
        self.th32ModuleID = 1 # No Longer Used
        self.th32ProcessID = th32ProcessID
        self.GlblcntUsage = 0xFFFF
        self.ProccntUsage = 0xFFFF
        self.modBaseAddr = modBaseAddr
        self.modBaseSize = modBaseSize
        self.hModule = hModule
        self.szModule = szModule
        self.szExePath = szExePath

    def writeToMemoryA(self, uc: Uc, address):
        packedStruct = pack('<IIIIIIII256s260s', self.dwSizeA, self.th32ModuleID, self.th32ProcessID, self.GlblcntUsage, self.ProccntUsage, self.modBaseAddr, self.modBaseSize, self.hModule, self.szModule.encode('ascii'), self.szExePath.encode('ascii'))
        uc.mem_write(address, packedStruct)

    def readFromMemoryA(self, uc: Uc, address):
        data = uc.mem_read(address, self.dwSizeA)
        unpackedStruct = unpack('<IIIIIIII256s260s', data)
        self.dwSizeA = unpackedStruct[0]
        self.th32ModuleID = unpackedStruct[1]
        self.th32ProcessID = unpackedStruct[2]
        self.GlblcntUsage = unpackedStruct[3]
        self.ProccntUsage = unpackedStruct[4]
        self.modBaseAddr = unpackedStruct[5]
        self.modBaseSize = unpackedStruct[6]
        self.hModule = unpackedStruct[7]
        self.szModule = unpackedStruct[8].decode()
        self.szExePath = unpackedStruct[9].decode()

    def writeToMemoryW(self, uc: Uc, address):
        packedStruct = pack('<IIIIIIII512s520s', self.dwSizeW, self.th32ModuleID, self.th32ProcessID, self.GlblcntUsage, self.ProccntUsage, self.modBaseAddr, self.modBaseSize, self.hModule, self.szModule.encode('utf-16')[2:], self.szExePath.encode('utf-16')[2:])
        uc.mem_write(address, packedStruct)

    def readFromMemoryW(self, uc: Uc, address):
        data = uc.mem_read(address, self.dwSizeW)
        unpackedStruct = unpack('<IIIIIIII512s520s', data)
        self.dwSizeW = unpackedStruct[0]
        self.th32ModuleID = unpackedStruct[1]
        self.th32ProcessID = unpackedStruct[2]
        self.GlblcntUsage = unpackedStruct[3]
        self.ProccntUsage = unpackedStruct[4]
        self.modBaseAddr = unpackedStruct[5]
        self.modBaseSize = unpackedStruct[6]
        self.hModule = unpackedStruct[7]
        self.szModule = unpackedStruct[8].decode()
        self.szExePath = unpackedStruct[9].decode()

class struct_SYSTEMTIME:
    # Backs SYSTEMTIME, *PSYSTEMTIME, *LPSYSTEMTIME
    def __init__(self, utc: bool, customTime= 0):
        if utc:
            if customTime == 0:
                timeVal = gmtime()
            else:
                timeVal = gmtime(customTime)
        else:
            if customTime == 0:
                timeVal = localtime()
            else:
                timeVal = localtime(customTime)

        self.wYear = timeVal.tm_year
        self.wMonth = timeVal.tm_mon
        dayOfWeek = timeVal.tm_wday + 1 # Convert Monday 0 to Sunday 0
        if dayOfWeek is 7: dayOfWeek = 0
        self.wDayOfWeek = dayOfWeek
        self.wDay = timeVal.tm_mday
        self.wHour = timeVal.tm_hour
        self.wMinute = timeVal.tm_min
        self.wSecond = timeVal.tm_sec
        self.wMilliseconds = 0

    def writeToMemory(self, uc: Uc, address):
        packedStruct = pack('<HHHHHHHH', self.wYear, self.wMonth, self.wDayOfWeek, self.wDay, self.wHour, self.wMinute, self.wSecond, self.wMilliseconds)
        uc.mem_write(address, packedStruct)

    def readFromMemory(self, uc: Uc, address):
        data = uc.mem_read(address, 16)
        unpackedStruct = unpack('<HHHHHHHH', data)
        self.wYear = unpackedStruct[0]
        self.wMonth = unpackedStruct[1]
        self.wDayOfWeek = unpackedStruct[2]
        self.wDay = unpackedStruct[3]
        self.wHour = unpackedStruct[4]
        self.wMinute = unpackedStruct[5]
        self.wSecond = unpackedStruct[6]
        self.wMilliseconds = unpackedStruct[7]