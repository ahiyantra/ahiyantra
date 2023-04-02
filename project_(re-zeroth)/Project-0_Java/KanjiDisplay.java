import java.awt.BorderLayout;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.Timer;
import java.io.InputStream;
import java.io.FileInputStream;
import java.io.BufferedInputStream;
import java.nio.charset.StandardCharsets;

public class KanjiDisplay {
    private JFrame frame;
    private JLabel kanjiLabel;
    private JPanel mainPanel;
    //private JButton closeButton;
    private JButton randomizeButton;
    private Timer timer;

    /*
    private String[] kanjiSymbols = {
        "\u4E00", "\u4E01", "\u4E02", "\u4E03", "\u4E04", // Add more kanji symbols here
    };
    */
    
    public KanjiDisplay() {

        frame = new JFrame("Randomly Chosen Japanese Kanji Font Symbol Display");

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        kanjiLabel = new JLabel("\u3087\u3045\u3053\u305D\u0021");

        //kanjiLabel.setFont(new Font("MS Mincho", Font.BOLD, 96));

        try {

        InputStream isTemp = new BufferedInputStream(new FileInputStream("msmincho.ttf"));

        Font font = Font.createFont(Font.TRUETYPE_FONT, isTemp);

        Font fontBase = font.deriveFont(Font.BOLD, 120f); // 96f
        kanjiLabel.setFont(fontBase);  

        } catch (Exception e) {

        System.out.println (e.getMessage());
        
        }

        System.out.println("\nWarning: Add the japanese font files to the same folder for avoiding the program exiting suddenly.\n");
        System.out.println("\nWarning: Change the system & software settings to include japanese if necessary for avoiding a blank display.\n");

        kanjiLabel.setHorizontalAlignment(JLabel.CENTER);
        
        mainPanel = new JPanel(new BorderLayout());
        frame.getContentPane().add(mainPanel);

        /*
        closeButton = new JButton("Close");
        closeButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                System.exit(0);
            }
        });
        mainPanel.add(closeButton, BorderLayout.NORTH);
        */

        randomizeButton = new JButton("Randomize");
        randomizeButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                updateSymbol();
            }
        });
        mainPanel.add(randomizeButton, BorderLayout.SOUTH);

        mainPanel.add(kanjiLabel, BorderLayout.CENTER);

        frame.setSize(500, 300); // instead of "pack"
        frame.setLocationRelativeTo(null);

        frame.setResizable(true); // false

        frame.setVisible(true);

        /*
        timer = new Timer(60000, new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                int randomIndex = new Random().nextInt(kanjiSymbols.length);
                kanjiLabel.setText(kanjiSymbols[randomIndex]);
            }
        });
        timer.start();
        */

        startUpdating();

    }

    private void startUpdating() {

        System.out.println("\nset japanese kanji font symbol\n");

        // Create a new random number generator
        Random rand = new Random();
        
        // Print a random kanji symbol every minute
        while (true) {
            String kanjiSymbol = "" + (char) (rand.nextInt(0x9fbf - 0x4e00 + 1) + 0x4e00); // Generate a random kanji character
            //System.out.println(kanji);
            kanjiLabel.setText(kanjiSymbol);

            try {
                Thread.sleep(60000); // wait 1 minute
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("\nchanged japanese kanji font symbol\n");

        }

    }

    private void updateSymbol() {

        Random newRand = new Random();

        String kanjiSymbol = "" + (char) (newRand.nextInt(0x9fbf - 0x4e00 + 1) + 0x4e00); // Generate a random kanji character
        
        kanjiLabel.setText(kanjiSymbol);
        
        System.out.println("\nrandomized japanese kanji font symbol\n");
    }

    public static void main(String[] args) {
        new KanjiDisplay();
    }
}
