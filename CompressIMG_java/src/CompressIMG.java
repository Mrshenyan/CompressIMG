import com.tinify.Source;
import com.tinify.Tinify;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;

public class CompressIMG extends JFrame {

    static int Window_with=640,Window_height = 200;
    public CompressIMG(){
        setSize(Window_with,Window_height);
        setTitle("Tinify压缩图片");
        setResizable(false);
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        int x = screenSize.width/2;
        int y = screenSize.height/2;
        setLocation(x,y);
        this.setLayout(null);
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
    }
    public static void main(String[] args){
        CompressIMG compressIMG = new CompressIMG();
        compressIMG.setVisible(true);
        addComponents(compressIMG);
    }

    private static void addComponents(CompressIMG compressIMG){

        JPanel winPanel = new JPanel();
        winPanel.setVisible(true);
        winPanel.setBounds(0,0,Window_with,Window_height);

        JLabel keyLab = new JLabel();
        keyLab.setText("Tinify密钥：");
        keyLab.setFont(new Font(null,Font.PLAIN,20));
        keyLab.setLocation(10,80);
        keyLab.setVisible(true);
        JTextField KeyTextField = new JTextField(30);
        KeyTextField.setSize(200,20);
        KeyTextField.setFont(new Font(null,Font.PLAIN,20));
        KeyTextField.replaceSelection("");
        KeyTextField.setVisible(true);
        KeyTextField.setLocation(100,80);
        KeyTextField.setBackground(Color.LIGHT_GRAY);

        JLabel fileTitle = new JLabel();
        fileTitle.setText("文件 路径：");
        fileTitle.setFont(new Font(null,Font.PLAIN,20));
        fileTitle.setLocation(10,80);
        fileTitle.setVisible(true);
        JTextField fileRoad = new JTextField(30);
        fileRoad.setSize(200,20);
        fileRoad.setFont(new Font(null,Font.PLAIN,20));
        fileRoad.setText("");
        fileRoad.setVisible(true);
        fileRoad.setLocation(100,80);
        fileRoad.setBackground(Color.LIGHT_GRAY);

        JProgressBar progressLab = new JProgressBar();
        progressLab.setValue(0);
        progressLab.setStringPainted(true);
        progressLab.setName("progress");
        progressLab.setVisible(true);
        JButton goBtn = new JButton();
        goBtn.setText("GO!");
        goBtn.setFont(new Font(null,Font.PLAIN,20));
        goBtn.setVisible(true);
        goBtn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    goBtnCallBack(fileRoad.getText(),KeyTextField.getText(),winPanel);
                } catch (IOException ioException) {
                    ioException.printStackTrace();
                }
            }
        });
        winPanel.add(keyLab);
        winPanel.add(KeyTextField);
        winPanel.add(fileTitle);
        winPanel.add(fileRoad);
        winPanel.add(progressLab);
        winPanel.add(goBtn);
        compressIMG.setContentPane(winPanel);
    }

    public static void goBtnCallBack(String url,String key,JPanel panel) throws IOException {
        if(key.isEmpty()){
            JOptionPane.showMessageDialog(panel,"密钥呢？？？");
        }else{
//            JOptionPane.showMessageDialog(panel,"开始了~");
            CompressURIMG(url,key,panel);
        }
    }

    private static void CompressURIMG(String url,String key,JPanel panel) throws IOException {
        Tinify.setKey(key);
        String URL = url.replaceAll("\\\\","/");
        File fileLists = new File(URL);
        JProgressBar progre = null;
        for (Component com : panel.getComponents()){
            if(com.getName()=="progress"){
                progre = (JProgressBar)com;
                progre.setValue(0);
            }
        }
        if(!fileLists.exists()){
            JOptionPane.showMessageDialog(panel,"指定路径不存在~");
        }else{
//            JOptionPane.showMessageDialog(panel,"压缩！");
            if(fileLists.list().length>0){
                int i=0;
                JDialog jop = new JDialog();
                JLabel jopLab = new JLabel();
                jop.setTitle("压缩中");
                jop.setSize(180,108);
                jop.setResizable(false);
                jop.setContentPane(jopLab);
                jop.setLocationRelativeTo(panel);
                jop.setModal(true);
                jopLab.setVisible(true);
                for(File file : fileLists.listFiles()){
                    if(file.getName().endsWith(".png")||file.getName().endsWith(".jpg")){
                        System.out.println("压缩开始.....");
                        String fileName = file.getName();
                        System.out.println(URL+"/"+fileName);
                        Source source = Tinify.fromFile(URL+"/"+fileName);
                        source.toFile(URL + "/" + fileName);
                        i++;
                        int pro = i/fileLists.list().length*100;
                        progre.setValue(pro);
                    }else{
                        JOptionPane.showMessageDialog(panel,"这里没有图片资源哦~");
                    }
                }
                if(i>=fileLists.listFiles().length){
                    JOptionPane.showMessageDialog(panel,"图片压缩完成！");
                }
            }else{
                JOptionPane.showMessageDialog(panel,"指定的路径下没有文件~");
            }
        }
    }


}
