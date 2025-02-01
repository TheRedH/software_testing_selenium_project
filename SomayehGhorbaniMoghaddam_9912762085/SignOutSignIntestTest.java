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

public class SignOutSignIntestTest {
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
  public void signOutSignIntest() {
    driver.get("https://www.truecar.com/");
    driver.manage().window().setSize(new Dimension(1936, 1048));
    driver.findElement(By.cssSelector("#menu-popover > .mt-\\[1px\\]")).click();
    driver.findElement(By.cssSelector(".py-1:nth-child(7) .text-base")).click();
    driver.findElement(By.cssSelector("#globalNavSignUp > span")).click();
    driver.findElement(By.cssSelector("*[data-test=\"regEmailField\"]")).sendKeys("test.tucar@gmail.ir");
    driver.findElement(By.cssSelector("*[data-test=\"submitButton\"]")).click();
    driver.findElement(By.cssSelector("*[data-test=\"regPasswordField\"]")).sendKeys("asd123");
    driver.findElement(By.cssSelector(".btn-fade")).click();
    {
      WebElement element = driver.findElement(By.cssSelector(".btn-fade"));
      Actions builder = new Actions(driver);
      builder.moveToElement(element).perform();
    }
    {
      WebElement element = driver.findElement(By.tagName("body"));
      Actions builder = new Actions(driver);
      builder.moveToElement(element, 0, 0).perform();
    }
  }
}
