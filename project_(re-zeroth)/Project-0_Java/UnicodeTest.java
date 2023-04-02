import java.awt.GridLayout;

import javax.swing.JFrame;
import javax.swing.JLabel;

public class UnicodeTest {

  public static void main(String args[]) {

    UnicodeDemo unicodeJFrame = new UnicodeDemo();
    unicodeJFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    unicodeJFrame.setSize(350, 250);
    unicodeJFrame.setVisible(true);

  } 
}

class UnicodeDemo extends JFrame {

  public UnicodeDemo() {

    super("Demonstrating Unicode Usage");

    setLayout(new GridLayout(8, 1));

    JLabel englishJLabel = new JLabel("\u0057\u0065\u006C\u0063" + "\u006F\u006D\u0065\u0020\u0074\u006F\u0020Unicode\u0021");
    englishJLabel.setToolTipText("This is English");
    add(englishJLabel);

    JLabel chineseJLabel = new JLabel("\u6B22\u8FCE\u4F7F\u7528" + "\u0020\u0020Unicode\u0021");
    chineseJLabel.setToolTipText("This is Traditional Chinese");
    add(chineseJLabel);

    JLabel cyrillicJLabel = new JLabel("\u0414\u043E\u0431\u0440" + "\u043E\u0020\u043F\u043E\u0436\u0430\u043B\u043E\u0432" + "\u0430\u0422\u044A\u0020\u0432\u0020Unicode\u0021");
    cyrillicJLabel.setToolTipText("This is Russian");
    add(cyrillicJLabel);

    JLabel frenchJLabel = new JLabel("\u0042\u0069\u0065\u006E\u0076" + "\u0065\u006E\u0075\u0065\u0020\u0061\u0075\u0020Unicode\u0021");
    frenchJLabel.setToolTipText("This is French");
    add(frenchJLabel);

    JLabel germanJLabel = new JLabel("\u0057\u0069\u006C\u006B\u006F" + "\u006D\u006D\u0065\u006E\u0020\u007A\u0075\u0020Unicode\u0021");
    germanJLabel.setToolTipText("This is German");
    add(germanJLabel);

    JLabel japaneseJLabel = new JLabel("Unicode\u3078\u3087\u3045" + "\u3053\u305D\u0021");
    japaneseJLabel.setToolTipText("This is Japanese");
    add(japaneseJLabel);

    JLabel portugueseJLabel = new JLabel("\u0053\u00E9\u006A\u0061"
        + "\u0020\u0042\u0065\u006D\u0076\u0069\u006E\u0064\u006F\u0020" + "Unicode\u0021");
    portugueseJLabel.setToolTipText("This is Portuguese");
    add(portugueseJLabel);

    JLabel spanishJLabel = new JLabel("\u0042\u0069\u0065\u006E"
        + "\u0076\u0065\u006E\u0069\u0064\u0061\u0020\u0061\u0020" + "Unicode\u0021");
    spanishJLabel.setToolTipText("This is Spanish");
    add(spanishJLabel);

  } 
}