import java.rmi.Remote;
import java.rmi.RemoteException;
import java.util.Map;

/**
 * Remote interface for academic progress evaluation.
 */
public interface StudentService extends Remote {

    String registerResult(String code, String learner, int score)
            throws RemoteException;

    Map<String, Object> getResult(String code)
            throws RemoteException;

    String academicStatus(String code)
            throws RemoteException;
}
