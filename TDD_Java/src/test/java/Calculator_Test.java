
import org.junit.Assert;
import org.junit.Before;

/**
 * Date: 1/12/15
 *
 * Description: Test Class for Calculator
 */


public class Calculator_Test {

    private Calculator testCalculator;

    @Before
    public void init(){
        testCalculator = new Calculator();
    }



     //You probably should rename this test case
    public void firstTest(){
        Assert.assertEquals("Expecting: 3", 3, testCalculator.add("1,2"));
    }
}
