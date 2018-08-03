import java.io.File;
import java.io.IOException;
import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.util.PDFTextStripper;
import org.apache.pdfbox.util.PDFTextStripperByArea;
import java.awt.Rectangle;
import java.util.List;
import org.apache.pdfbox.pdmodel.PDPage;

public class nocr {

    static float pwidth;
    static float pheight;

    private static int widthByPercent(double percent) {
        return (int)Math.round(percent * pwidth);
    }

    private static int heightByPercent(double percent) {
        return (int)Math.round(percent * pheight);
    }

    public static void main(String[] args) {

        try {
            //Create objects
            File file = new File("C:\\Users\\Andrew Riffle\\IdeaProjects\\I9PDFExtractor\\nocr\\ 2011_i9_test_noPIV.pdf");
            PDDocument document = PDDocument.load(file);
            PDFTextStripperByArea stripper = new PDFTextStripperByArea();

            //Get the first page
            List<PDPage> allPages = document.getDocumentCatalog().getAllPages();
            PDPage page = allPages.get(0);

            //Convert to percentages, safer to use on variable sized documents and easier to use
            //height = 841.8901 width = 595.28
            pheight = page.getMediaBox().getHeight() / 100;
            pwidth = page.getMediaBox().getWidth() / 100;

            //Define the areas to search
            //Rectangle(upperleft_x, upperleft_y, width, height)
            Rectangle fullname = new Rectangle(widthByPercent(2.5), heightByPercent(19), widthByPercent(67), heightByPercent(1));
            Rectangle lname = new Rectangle(widthByPercent(9), heightByPercent(18.7), widthByPercent(23), heightByPercent(1));
            Rectangle fname = new Rectangle(widthByPercent(36), heightByPercent(18.7), widthByPercent(23), heightByPercent(1));
           Rectangle middleinit = new Rectangle(widthByPercent(61.5), heightByPercent(18.7), widthByPercent(26), heightByPercent(1));
           Rectangle maiden = new Rectangle(widthByPercent(71), heightByPercent(18.7), widthByPercent(26), heightByPercent(1));
            Rectangle address = new Rectangle(widthByPercent(3), heightByPercent(22), widthByPercent(40), heightByPercent(1));
            Rectangle apt = new Rectangle(widthByPercent(58), heightByPercent(22), widthByPercent(11), heightByPercent(1));
            Rectangle dob = new Rectangle(widthByPercent(70), heightByPercent(22), widthByPercent(21), heightByPercent(1));
            Rectangle city = new Rectangle(widthByPercent(3), heightByPercent(26), widthByPercent(26), heightByPercent(1));
            Rectangle state = new Rectangle(widthByPercent(32), heightByPercent(26), widthByPercent(11), heightByPercent(1));
            Rectangle zip = new Rectangle(widthByPercent(58), heightByPercent(26), widthByPercent(11), heightByPercent(1));
            Rectangle ssn = new Rectangle(widthByPercent(70), heightByPercent(26), widthByPercent(16.5), heightByPercent(1));
            Rectangle citizen = new Rectangle(widthByPercent(48.5), heightByPercent(29.5), widthByPercent(40), heightByPercent(1));
            Rectangle national = new Rectangle(widthByPercent(48.5), heightByPercent(31), widthByPercent(40), heightByPercent(1));
            Rectangle resident = new Rectangle(widthByPercent(48.5), heightByPercent(33), widthByPercent(40), heightByPercent(1));
            Rectangle alien = new Rectangle(widthByPercent(48.5), heightByPercent(35), widthByPercent(40), heightByPercent(1));
            Rectangle translatorname = new Rectangle(widthByPercent(52), heightByPercent(44.5), widthByPercent(25), heightByPercent(1));
            Rectangle translatoraddress = new Rectangle(widthByPercent(8), heightByPercent(48), widthByPercent(40), heightByPercent(1));
            Rectangle translatordate = new Rectangle(widthByPercent(70), heightByPercent(48), widthByPercent(20), heightByPercent(1));
            Rectangle boxAdoctitle = new Rectangle(widthByPercent(12), heightByPercent(56), widthByPercent(21.5), heightByPercent(1));
            Rectangle boxAissuer = new Rectangle(widthByPercent(13), heightByPercent(58), widthByPercent(20), heightByPercent(1));
            Rectangle boxAdocnumber1 = new Rectangle(widthByPercent(10.5), heightByPercent(60.5), widthByPercent(20), heightByPercent(1));
            Rectangle boxAexpiration1 = new Rectangle(widthByPercent(20.5), heightByPercent(62), widthByPercent(20), heightByPercent(1));
            Rectangle boxAdocnumber2 = new Rectangle(widthByPercent(10.5), heightByPercent(64), widthByPercent(20), heightByPercent(1));
            Rectangle boxAexpiration2 = new Rectangle(widthByPercent(20.5), heightByPercent(66), widthByPercent(20), heightByPercent(1));
            Rectangle boxBline1 = new Rectangle(widthByPercent(38.5), heightByPercent(56.5), widthByPercent(20), heightByPercent(1));
            Rectangle boxBline2 = new Rectangle(widthByPercent(38.5), heightByPercent(58.5), widthByPercent(20), heightByPercent(1));
            Rectangle boxBline3 = new Rectangle(widthByPercent(38.5), heightByPercent(60.5), widthByPercent(20), heightByPercent(1));
            Rectangle boxBline4 = new Rectangle(widthByPercent(38.5), heightByPercent(62.5), widthByPercent(20), heightByPercent(1));
            Rectangle boxCline1 = new Rectangle(widthByPercent(72.5), heightByPercent(56.5), widthByPercent(20), heightByPercent(1));
            Rectangle boxCline2 = new Rectangle(widthByPercent(72.5), heightByPercent(58.5), widthByPercent(20), heightByPercent(1));
            Rectangle boxCline3 = new Rectangle(widthByPercent(72.5), heightByPercent(60.5), widthByPercent(20), heightByPercent(1));
            Rectangle boxCline4 = new Rectangle(widthByPercent(72.5), heightByPercent(62.5), widthByPercent(20), heightByPercent(1));
            Rectangle formvertop = new Rectangle(widthByPercent(0), heightByPercent(0), widthByPercent(100), heightByPercent(8));
            Rectangle formverbottom = new Rectangle(widthByPercent(0), heightByPercent(92), widthByPercent(100), heightByPercent(8));
            Rectangle examinername = new Rectangle(widthByPercent(39), heightByPercent(75.5), widthByPercent(20), heightByPercent(1));
            Rectangle examinertitle = new Rectangle(widthByPercent(71), heightByPercent(75.5), widthByPercent(20), heightByPercent(1));
            Rectangle examinerbusiness_address = new Rectangle(widthByPercent(2), heightByPercent(78), widthByPercent(67), heightByPercent(1));
            Rectangle boxCline4 = new Rectangle(widthByPercent(72.5), heightByPercent(62.5), widthByPercent(20), heightByPercent(1));


            stripper.addRegion("lastName", translatorname);

            //Search the area and print the found text
            stripper.setSortByPosition(true);
            stripper.extractRegions(page);
            String text = stripper.getTextForRegion(stripper.getRegions().get(0));
            System.out.println(text);

        } catch (Exception e){
            System.out.println(e.getMessage());
        }
    }
}