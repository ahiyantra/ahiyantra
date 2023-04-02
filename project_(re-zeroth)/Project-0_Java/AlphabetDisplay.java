import java.awt.*;
import javax.swing.*;
import java.util.Random;
import java.io.InputStream;
import java.io.FileInputStream;
import java.io.BufferedInputStream;
import java.nio.charset.StandardCharsets;

public class AlphabetDisplay {

    private JLabel alphabetLabel;

    public AlphabetDisplay() {
        JFrame frame = new JFrame("Randomly Chosen English Alphabet Font Symbol Display");

        alphabetLabel = new JLabel("\u0057\u0065\u006C\u0063"
        + "\u006F\u006D\u0065\u0021", SwingConstants.CENTER);

        //alphabetLabel.setFont(new Font("Arial", Font.BOLD, 72));

        try {

        InputStream isTemp = new BufferedInputStream(new FileInputStream("arial.ttf"));

        Font font = Font.createFont(Font.TRUETYPE_FONT, isTemp);

        Font fontBase = font.deriveFont(Font.BOLD, 120f); // 72f
        alphabetLabel.setFont(fontBase);  

        } catch (Exception e) {

        System.out.println (e.getMessage());

        }

        System.out.println("\nWarning: Add the english font files to the same folder for avoiding the program exiting suddenly.\n");
        System.out.println("\nWarning: Change the system & software settings to include english if necessary for avoiding a blank display.\n");

        frame.add(alphabetLabel, BorderLayout.CENTER);

        /*
        JButton closeButton = new JButton("Close");
        closeButton.addActionListener(e -> System.exit(0));
        frame.add(closeButton, BorderLayout.NORTH);
        */

        JButton randomizeButton = new JButton("Randomize");
        randomizeButton.addActionListener(e -> updateSymbol());
        frame.add(randomizeButton, BorderLayout.SOUTH);

        frame.setSize(500, 300); // instead of "pack"
        frame.setLocationRelativeTo(null);
        frame.setResizable(true); // false
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        frame.setVisible(true);

        startUpdating();
    }

    private void startUpdating() {

        System.out.println("\nset english alphabet font symbol\n");

        Random rand = new Random();

        char randomChar = (char) (rand.nextInt(26) + 'A');
        alphabetLabel.setText(String.valueOf(randomChar));


        Timer timer = new Timer(60000, e -> {

            Random newRand = new Random();

            char newRandomChar = (char) (newRand.nextInt(26) + 'A');
            alphabetLabel.setText(String.valueOf(newRandomChar));

            System.out.println("\nchanged english alphabet font symbol\n");
        });

        timer.setRepeats(true);
        timer.start();

    }

    private void updateSymbol() {

        Random newerRand = new Random();

        char newerRandomChar = (char) (newerRand.nextInt(26) + 'A');
        alphabetLabel.setText(String.valueOf(newerRandomChar));
        
        System.out.println("\nrandomized english alphabet font symbol\n");
    }

    public static void main(String[] args) {
        new AlphabetDisplay();
    }
}
