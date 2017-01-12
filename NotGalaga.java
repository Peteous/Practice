package Galaga;
import java.awt.event.KeyEvent;
import javax.swing.JApplet;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.Color;
import java.awt.event.KeyListener;
public class NotGalaga extends JApplet implements KeyListener{
    private Image ship, alien;
    private Ship you = new Ship();
    private Image offScreen;
    private Alien borg = new Alien();
    private Graphics JimmyBuffet;
    @Override public void init()
    {
        ship = getImage(getDocumentBase(), "Ship.png");
        alien = getImage(getDocumentBase(),"Alien.png");
        setSize(512,512);
        offScreen = createImage(512,512);
        JimmyBuffet = offScreen.getGraphics();
        setBackground(Color.black);
        this.addKeyListener(this);
    }
    @Override public void paint(Graphics page)
    {
        JimmyBuffet.clearRect(0,0,512,512);
        JimmyBuffet.setColor(Color.black);
        JimmyBuffet.fillRect(0, 0, 512, 512);
        you.act(); borg.act();
        JimmyBuffet.drawImage(alien, borg.getX(), borg.getY(), this);
        JimmyBuffet.drawImage(ship, you.getX(), you.getY(), this);
        JimmyBuffet.setColor(Color.gray);JimmyBuffet.fillRect(0,496,512,16);
        page.drawImage(offScreen,0,0,null);
        repaint();
    }
    @Override public void keyTyped(KeyEvent e) {/*throw new UnsupportedOperationException("Not supported yet.");*/}
    @Override public void keyPressed(KeyEvent e)
    {
        int key = e.getKeyCode();
        switch(key)
        {
            case KeyEvent.VK_UP:
                you.setYspd(-2); break;
            case KeyEvent.VK_DOWN:
                you.setYspd(2); break;
            case KeyEvent.VK_LEFT:
                you.setXspd(-2); break;
            case KeyEvent.VK_RIGHT:
                you.setXspd(2); break;
        }
        repaint();
    }
    @Override public void keyReleased(KeyEvent e) {
        int key = e.getKeyCode();
        switch(key)
        {
            case KeyEvent.VK_UP:
                you.setYspd(-0); break;
            case KeyEvent.VK_DOWN:
                you.setYspd(0); break;
            case KeyEvent.VK_LEFT:
                you.setXspd(0); break;
            case KeyEvent.VK_RIGHT:
                you.setXspd(0); break;
        }
    }
}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
package Galaga;
public class Ship extends Object{
    protected int xpos,ypos; protected double xspeed = 0,yspeed = 0,xposi = 256-24,yposi = 400;
    public Ship()
    {
        ypos = 512-96; xpos = 256-24;
    }
    public int getX(){return xpos;}
    public void setX(double xpos){this.xposi = xpos; return;}
    public int getY(){return ypos;}
    public void setY(double ypos){this.yposi = ypos;}
    public void act()
    {
        move();
    }
    public void move()
    {
        xposi = xposi + xspeed;
        yposi+=yspeed;
        if(yposi > 512-64)
            yposi = 512-64;
        if(xposi >512-48)
            xposi = 512-48;
        if(yposi < 0)
            yposi = 0;
        if(xposi <0)
            xposi = 0;
        xpos = (int) (xposi);
        ypos = (int) (yposi);
    }
    public void setXspd(double speed){xspeed = speed;}
    public void setYspd(double speed){yspeed = speed;}
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
package Galaga;
public class Alien extends Ship{
    private double i=0,sin=0,cos=0;
    public void Alien()
    {
        setX(256); setY(1);
        xposi = 256-24; yposi = 0;
    }
    @Override public void act()
    {
        if (i > 100) {
            i = 0;
        }
        i+=.01;
        sin= Math.sin(i)/5;
        cos= Math.cos(i)/5;
        setYspd(sin);
        setXspd(cos);

        move()
                ;
    }
}
