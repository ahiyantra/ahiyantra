import java.applet.*;
import java.awt.*;

public class Main0 extends Applet {
   public void init() {  
      picture = getImage(getDocumentBase(),"Opera Snapshot_2018-11-23_170156_en.wikipedia.org.png");  
   }
   public void paint(Graphics g) {
      g.drawString("A Java Applet for displaying Kanji and Kana",50,50);
      g.drawString("?",100,100);
      g.drawImage(picture, 150,150, this);  
   }
   
   Image picture;  
  
     
    
   
}

    
      