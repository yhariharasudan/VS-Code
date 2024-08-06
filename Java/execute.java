import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.lang.management.ManagementFactory;
import com.sun.management.OperatingSystemMXBean;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

public class execute {
    public static void main(String[] args) {
        OperatingSystemMXBean osMXBean = (OperatingSystemMXBean) ManagementFactory.getOperatingSystemMXBean();

        System.out.println("Operating System Name: " + osMXBean.getName());
        System.out.println("Version: " + osMXBean.getVersion());
        System.out.println("CPU Count: " + osMXBean.getAvailableProcessors());
        System.out.println("Architecture: " + osMXBean.getArch());
        System.out.println("System CPU Load: " + osMXBean.getSystemCpuLoad());
        System.out.println("Process CPU Load: " + osMXBean.getProcessCpuLoad());
        System.out.println("System Average Load: " + osMXBean.getSystemLoadAverage());

        System.out.println("RAM Free: " + osMXBean.getFreePhysicalMemorySize() / 1048576 + " MB");
        System.out.println("RAM Total: " + osMXBean.getTotalPhysicalMemorySize() / 1048576 + " MB");

        // Get a list of all running processes
        List<ProcessHandle> allProcesses = ProcessHandle.allProcesses().collect(Collectors.toList());
        System.out.println("\nRunning Processes:");
        for (ProcessHandle process : allProcesses) {
            Optional<String> commandLine = process.info().commandLine();
            String shortFormName = commandLine.map(cmd -> {
                String[] parts = cmd.split("\\s+");
                return parts[0].substring(parts[0].lastIndexOf("/") + 1);
            }).orElse("Unknown");

            if (shortFormName.equals("k3s")) {
                System.out.println("PID: " + process.pid() + ", Command: " + shortFormName);
                try {
                    // Execute the ps command to get CPU usage
                    Process psProcess = new ProcessBuilder("ps", "-p", String.valueOf(process.pid()), "-o", "%cpu").start();
                    BufferedReader reader = new BufferedReader(new InputStreamReader(psProcess.getInputStream()));
                    String line = reader.readLine(); // Skip the header line
                    line = reader.readLine(); // Read the CPU usage line
                    if (line != null) {
                        System.out.println("CPU Usage: " + line.trim() + "%");
                    }
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }
    }
}

