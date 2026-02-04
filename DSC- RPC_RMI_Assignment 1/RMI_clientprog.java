import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Map;

/**
 * RMI Client
 */
public class RMIClient {

    public static void main(String[] args) {
        try {
            Registry registry =
                LocateRegistry.getRegistry("EC2_PUBLIC_IP", 1099);

            StudentService service =
                (StudentService) registry.lookup("StudentService");

            System.out.println(
                service.registerResult("AC301", "Kow", 74)
            );

            Map<String, Object> result =
                service.getResult("AC301");

            System.out.println("Result Summary: " + result);
            System.out.println(
                "Academic Status: " +
                service.academicStatus("AC301")
            );

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
