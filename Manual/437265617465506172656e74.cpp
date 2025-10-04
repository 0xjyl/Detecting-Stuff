/*
------------------------------------------------------------
 Status:       NOT VALIDATED YET!!! Needs work 10/04/25
 Author:       0xjyl
 Description:  A Windows process lineage manipulation utility that spawns a new process under a spoofed parent using the PROC_THREAD_ATTRIBUTE_PARENT_PROCESS attribute via STARTUPINFOEX.

 Purpose:      This program is used for manual detection testing by hopefully triggering detection logic surrounded by suspicious parent process creation events.

 Detection Relevance:
   - MITRE ATT&CK: T1134.004 (Parent PID Spoofing)
   - EDR Focus: Inconsistent process lineage, PPID mismatches, EXTENDED_STARTUPINFO_PRESENT flag usage, and anomalous OpenProcess calls with PROCESS_CREATE_PROCESS privileges.

 Build:
   Compile with a standard Windows C++ compiler (e.g., MSVC).
   Requires <windows.h> and <iostream>.

------------------------------------------------------------
*/

HANDLE GetParentHandle(DWORD parentPid) {
    HANDLE hProcess = OpenProcess(PROCESS_CREATE_PROCESS, FALSE, parentPid);
    if (!hProcess) {
        std::cerr << "Failed to open parent PID " << parentPid << std::endl;
        return nullptr;
    }
    return hProcess;
}


STARTUPINFOEX siex = { 0 };
PROCESS_INFORMATION pi = { 0 };
SIZE_T attrSize = 0;

InitializeProcThreadAttributeList(NULL, 1, 0, &attrSize);
siex.lpAttributeList = (LPPROC_THREAD_ATTRIBUTE_LIST)HeapAlloc(GetProcessHeap(), 0, attrSize);
InitializeProcThreadAttributeList(siex.lpAttributeList, 1, 0, &attrSize);

HANDLE hParent = GetParentHandle(parentPid);
UpdateProcThreadAttribute(siex.lpAttributeList, 0, PROC_THREAD_ATTRIBUTE_PARENT_PROCESS, &hParent, sizeof(HANDLE), NULL, NULL);

siex.StartupInfo.cb = sizeof(STARTUPINFOEX);

CreateProcessW(
    targetBinary.c_str(),
    NULL,
    NULL, NULL,
    FALSE,
    EXTENDED_STARTUPINFO_PRESENT,
    NULL, NULL,
    &siex.StartupInfo,
    &pi
);

DeleteProcThreadAttributeList(siex.lpAttributeList);
HeapFree(GetProcessHeap(), 0, siex.lpAttributeList);
CloseHandle(hParent);
CloseHandle(pi.hProcess);
CloseHandle(pi.hThread);

