package FINAL;


import java.sql.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


abstract public class Person {
    private String NAME;
    private String DATE_OF_BIRTH;

    public Person(){}
    public Person(String NAME, String DATE_OF_BIRTH) {
        this.setNAME(NAME);
        this.setDATE_OF_BIRTH(DATE_OF_BIRTH);
    }

    public String getNAME() {
        return NAME;
    }

    public void setNAME(String NAME) {
        Pattern p = Pattern.compile("^[ A-Za-z]+$");
        Matcher m = p.matcher(NAME);
        boolean b = m.matches();
        if (((!NAME.equals("")) && b) && !NAME.isBlank()) this.NAME = NAME;
        else System.out.println("Invalid input.");

    }

    public String getDATE_OF_BIRTH() {
        return DATE_OF_BIRTH;
    }
    public void setDATE_OF_BIRTH(String DATE_OF_BIRTH) { // yyyy-mm-dd
        String strDateRegEx = "((18|19|20)[0-9]{2}[\\-.](0[13578]|1[02])[\\-.](0[1-9]|[12][0-9]|3[01]))|(18|19|20)[0-9]{2}[\\-.](0[469]|11)[\\-.](0[1-9]|[12][0-9]|30)|(18|19|20)[0-9]{2}[\\-.](02)[\\-.](0[1-9]|1[0-9]|2[0-8])|(((18|19|20)(04|08|[2468][048]|[13579][26]))|2000)[\\-.](02)[\\-.]29\n";
        boolean isValid = false;
        if(DATE_OF_BIRTH.matches(strDateRegEx)){
            SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
            try{
                sdf.parse(DATE_OF_BIRTH);
                isValid = true;
            }catch(ParseException e){
                e.printStackTrace();
            }
        }
        if(isValid) this.DATE_OF_BIRTH = DATE_OF_BIRTH;
        else System.out.println("Incorrect date format format. Try again.");
    }

}
