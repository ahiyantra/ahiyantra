import java.awt.*;
import javax.swing.*;
import java.util.Random;
import java.io.InputStream;
import java.io.FileInputStream;
import java.io.BufferedInputStream;
import java.nio.charset.StandardCharsets;

public class KanaDisplay extends JFrame { // implements Runnable {
    
    private JLabel kanaLabel;
    
    public KanaDisplay() {
        setTitle("Randomly Chosen Japanese Kana Font Symbol Display");
        
        kanaLabel = new JLabel("\u3087\u3045\u3053\u305D\u0021", SwingConstants.CENTER);

        //kanaLabel.setHorizontalAlignment(SwingConstants.CENTER);

        //kanaLabel.setFont(new Font("MS Gothic", Font.BOLD, 72));

        try {

        //BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream("msgothic.ttc"), StandardCharsets.UTF_8));

        InputStream isTemp = new BufferedInputStream(new FileInputStream("msgothic.ttc"));

        //InputStream isTemp = getClass().getResourceAsStream("Gen-Jyuu-Gothic-Monospace-Bold.ttf");

        Font font = Font.createFont(Font.TRUETYPE_FONT, isTemp);

        Font fontBase = font.deriveFont(Font.BOLD, 120f); // 72f
        kanaLabel.setFont(fontBase);  // Japanese font

        } catch (Exception e) {

        System.out.println (e.getMessage());

        }

        System.out.println("\nWarning: Add the japanese font files to the same folder for avoiding the program exiting suddenly.\n");
        System.out.println("\nWarning: Change the system & software settings to include japanese if necessary for avoiding a blank display.\n");
        
        add(kanaLabel, BorderLayout.CENTER);
        
        /*
        JButton closeButton = new JButton("Close");
        closeButton.addActionListener(e -> System.exit(0));
        add(closeButton, BorderLayout.NORTH); // BorderLayout.SOUTH
        */
        
        JButton randomizeButton = new JButton("Randomize");
        randomizeButton.addActionListener(e -> updateSymbol());
        add(randomizeButton, BorderLayout.SOUTH); // BorderLayout.NORTH

        setSize(500, 300);
        setLocationRelativeTo(null);
        setResizable(true); // false
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        setVisible(true);

        startUpdating();
    }
    
    //@Override
    private void startUpdating() { // public

        System.out.println("\nset japanese kana font symbol\n");

        while (true) {

            Random rand = new Random();

            int kanaCode = rand.nextInt(96) + 0x3041; // Choose from kana unicode range
            char kanaChar = (char) kanaCode;
            kanaLabel.setText(Character.toString(kanaChar));

            try {
                Thread.sleep(60000); // wait 1 minute
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            System.out.println("\nchanged japanese kana font symbol\n");
        }
    }

    private void updateSymbol() {

        Random newRand = new Random();

        int kanaCode = newRand.nextInt(96) + 0x3041; // Choose from kana unicode range
        char kanaChar = (char) kanaCode;
        kanaLabel.setText(Character.toString(kanaChar));
        
        System.out.println("\nrandomized japanese kana font symbol\n");
    }
    
    public static void main(String[] args) {
        //SwingUtilities.invokeLater(() -> new KanaDisplay().run());
        new KanaDisplay();
    }
}
