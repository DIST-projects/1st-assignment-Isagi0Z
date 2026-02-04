import java.rmi.server.UnicastRemoteObject;
import java.rmi.RemoteException;
import java.util.HashMap;
import java.util.Map;

/**
 * Remote object implementation.
 */
public class StudentServiceImpl
        extends UnicastRemoteObject
        implements StudentService {

    private Map<String, Map<String, Object>> records;

    protected StudentServiceImpl() throws RemoteException {
        super();
        records = new HashMap<>();
    }

    public String registerResult(String code, String learner, int score) {
        Map<String, Object> data = new HashMap<>();
        data.put("learner", learner);
        data.put("score", score);
        records.put(code, data);
        return "Result registered successfully";
    }

    public Map<String, Object> getResult(String code) {
        return records.getOrDefault(code, null);
    }

    public String academicStatus(String code) {
        if (!records.containsKey(code))
            return "No record found";

        int score = (int) records.get(code).get("score");

        if (score >= 80) return "Outstanding";
        else if (score >= 60) return "Satisfactory";
        else return "Unsatisfactory";
    }
}
