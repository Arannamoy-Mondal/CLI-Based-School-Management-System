

public class exam{
    static String semester;
    public static double  totalMarks=80;
    private  double attainedMarks;
    public static void updateInfo(String sem,double tMarks) {
        semester=sem;
        totalMarks=tMarks;
    }

    public String toString(){
        return "Semester: "+semester+", Total marks: "+totalMarks+", Attained marks:"+attainedMarks;
    }

}