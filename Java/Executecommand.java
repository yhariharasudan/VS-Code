import oshi.SystemInfo;
import oshi.hardware.CentralProcessor;
import oshi.software.os.OSProcess;
import oshi.software.os.OperatingSystem;

import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class Executecommand {
    public static void main(String[] args) throws InterruptedException {
        SystemInfo si = new SystemInfo();
        CentralProcessor processor = si.getHardware().getProcessor();
        OperatingSystem os = si.getOperatingSystem();

        // Get the list of processes
        List<OSProcess> processes = Arrays.asList(os.getProcesses(0, OperatingSystem.ProcessSort.CPU));

        // Initial snapshot
        long[] prevTicks = processor.getSystemCpuLoadTicks();
        long[][] prevProcTicks = new long[processes.size()][CentralProcessor.TickType.values().length];

        for (int i = 0; i < processes.size(); i++) {
            prevProcTicks[i] = processes.get(i).getProcessorCpuLoadTicks();
        }

        // Wait for a second to get the next snapshot
        Thread.sleep(1000);

        // Next snapshot
        long[] ticks = processor.getSystemCpuLoadTicks();
        long[][] procTicks = new long[processes.size()][CentralProcessor.TickType.values().length];

        for (int i = 0; i < processes.size(); i++) {
            procTicks[i] = processes.get(i).getProcessorCpuLoadTicks();
        }

        System.out.println("Running Processes:");
        for (int i = 0; i < processes.size(); i++) {
            OSProcess process = processes.get(i);
            double cpuLoad = process.getProcessorCpuLoadBetweenTicks(prevProcTicks[i]);

            String command = process.getCommandLine();
            String shortFormName = command.split("\\s+")[0].substring(command.lastIndexOf("/") + 1);

            System.out.printf("PID: %d, Command: %s, CPU Usage: %.2f%%\n", process.getProcessID(), shortFormName, cpuLoad * 100);
        }
    }
}
