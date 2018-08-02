import java.io.File;
import java.io.IOException;
import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.util.PDFTextStripper;
import org.apache.pdfbox.util.PDFTextStripperByArea;
import java.awt.Rectangle;
import java.util.List;
import org.apache.pdfbox.pdmodel.PDPage;

public class nocr {
    public static void main(String[] args) {

        try {
            //Create objects
            File file = new File("/Users/doctor_ew/IdeaProjects/I9PDFExtractor/nocr/2011_i9_test_noPIV.pdf");
            PDDocument document = PDDocument.load(file);
            PDFTextStripperByArea stripper = new PDFTextStripperByArea();

            //Get the first page
            List<PDPage> allPages = document.getDocumentCatalog().getAllPages();
            PDPage page = allPages.get(0);

            //Convert to percentages, safer to use on variable sized documents and easier to use
            float pheight = page.getMediaBox().getHeight() / 100;
            float pwidth = page.getMediaBox().getWidth() / 100;

            //Define the areas to search
            //Rectangle(upperleft_x, upperleft_y, width, height
            Rectangle lname = new Rectangle((int)Math.round(9.5 * pwidth), (int)Math.round(18 * pheight), 159, 25);
            Rectangle fname = new Rectangle((int)Math.round(36 * pwidth), (int)Math.round(18 * pheight), 128, 25);
            Rectangle middleinit = new Rectangle((int)Math.round(36 * pwidth), (int)Math.round(18 * pheight), 128, 25);
            Rectangle maiden = new Rectangle((int)Math.round(36 * pwidth), (int)Math.round(18 * pheight), 128, 25);
            Rectangle address = new Rectangle((int)Math.round(3 * pwidth), (int)Math.round(21.5 * pheight), 128, 25);
            Rectangle apt = new Rectangle((int)Math.round(36 * pwidth), (int)Math.round(18 * pheight), 128, 25);
            Rectangle dob = new Rectangle((int)Math.round(60 * pwidth), (int)Math.round(18 * pheight), 128, 25);

            stripper.addRegion("lastName", address);

            //Search the area and print the found text
            stripper.extractRegions(page);
            stripper.setSortByPosition(true);
            String text = stripper.getTextForRegion(stripper.getRegions().get(0));
            System.out.println(text);

        } catch (Exception e){
            System.out.println(e.getMessage());
        }
    }
}