import org.junit.Test;
import org.junit.Before;
import org.junit.After;
import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.is;
import static org.hamcrest.core.IsNot.not;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Alert;
import org.openqa.selenium.Keys;
import java.util.*;
import java.net.MalformedURLException;
import java.net.URL;

public class ShowPassIcontestTest {
  private WebDriver driver;
  private Map<String, Object> vars;
  JavascriptExecutor js;
  @Before
  public void setUp() {
    driver = new ChromeDriver();
    js = (JavascriptExecutor) driver;
    vars = new HashMap<String, Object>();
  }
  @After
  public void tearDown() {
    driver.quit();
  }
  @Test
  public void showPassIcontest() {
    driver.get("https://www.truecar.com/");
    driver.manage().window().setSize(new Dimension(516, 1019));
    driver.findElement(By.cssSelector("#globalNavSignUpMobile > span")).click();
    driver.findElement(By.cssSelector("*[data-test=\"regEmailField\"]")).sendKeys("test.tucar@gmail.com");
    driver.findElement(By.cssSelector(".btn-fade")).click();
    driver.findElement(By.cssSelector("*[data-test=\"regPasswordField\"]")).sendKeys("test1234");
    driver.findElement(By.cssSelector(".top-\\[calc\\(0\\%\\+12px\\)\\] use")).click();
    driver.findElement(By.cssSelector(".btn-fade")).click();
  }
}
