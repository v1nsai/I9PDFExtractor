//import org.apache.pdfbox.pdmodel.PDDocument
//import org.apache.pdfbox.text.PDFTextStripperByArea
//import java.awt.Rectangle
//import org.apache.pdfbox.pdmodel.PDPage
//import java.nio.charset.StandardCharsets
//
//pwidth = 0.00
//pheight = 0.00
//
////Using percentages of page width and height is better at handling size variation than pixels
////These functions handle the conversion
//def widthByPercent(double percent) {
//    return (int)Math.round(percent * pwidth)
//}
//
//def heightByPercent(double percent) {
//    return (int)Math.round(percent * pheight)
//}
//
////Find the form version and load the JSON containing the proper coords
//def getFormVersion(PDPage page, PDFTextStripperByArea stripper) {
//    //Grab the top and bottom of the page, concatenate them and look for the Rev. date
//    Rectangle formvertop = new Rectangle(widthByPercent(0), heightByPercent(0), widthByPercent(100), heightByPercent(8))
//    stripper.addRegion("formvertop", formvertop)
//    Rectangle formverbottom = new Rectangle(widthByPercent(0), heightByPercent(92), widthByPercent(100), heightByPercent(8))
//    stripper.addRegion("formverbottom", formverbottom)
//    stripper.setSortByPosition(true)
//    stripper.extractRegions(page)
//    List<String> regions = stripper.getRegions()
//    String ver = ''
//    for (String region : regions) {
//        String swap = stripper.getTextForRegion(region)
//        ver = ver + swap
//    }
//
//    if(ver.contains('(Rev. 08/07/09)')){
//        return '08/07/09'
//    }
//}
//
//def getPageNumber(version, page, stripper) {
//    //Grab the top and bottom of the page, concatenate them and look for the Rev. date
//    Rectangle formvertop = new Rectangle(widthByPercent(0), heightByPercent(0), widthByPercent(100), heightByPercent(8))
//    stripper.addRegion("formvertop", formvertop)
//    Rectangle formverbottom = new Rectangle(widthByPercent(0), heightByPercent(92), widthByPercent(100), heightByPercent(8))
//    stripper.addRegion("formverbottom", formverbottom)
//    stripper.setSortByPosition(true)
//    stripper.extractRegions(page)
//    List<String> regions = stripper.getRegions()
//    String ver = ''
//    for (String region : regions) {
//        String swap = stripper.getTextForRegion(region)
//        ver = ver + swap
//    }
//    print(ver)
//    def m = ver =~ /(?!Page) \d/
//    if (m) {
//        return m.group()
//    }
//    else
//        return 'Page number not found'
//
//}
//
//def getCoords(String version, int pageNumber) {
//    def swapcoords = [:]
//    if(version.contains("08/07/09") && pageNumber == 0) {
//        swapcoords = [
//                'LastName': [0.02, 0.195, 0.27, 0.01],
//                'FirstName': [0.29, 0.195, 0.23, 0.01],
//                'MiddleInitial': [0.615, 0.195, 0.09, 0.01],
//                'MaidenName': [0.69, 0.195, 0.26, 0.01],
//                'StreetAddress': [0.03, 0.23, 0.54, 0.01],
//                'ApartmentNo': [0.57, 0.23, 0.12, 0.01],
//                'City': [0.02, 0.265, 0.26, 0.01],
//                'State': [0.305, 0.265, 0.2, 0.01],
//                'Zip': [0.56, 0.265, 0.11, 0.01],
//                'DateOfBirth': [0.7, 0.23, 0.21, 0.01],
//                'SocialSecurity': [0.70, 0.265, 0.165, 0.01],
//                'citizen': [0.485, 0.295, 0.40, 0.01],
//                'national': [0.485, 0.31, 0.40, 0.01],
//                'resident': [0.485, 0.33, 0.40, 0.01],
//                'alien': [0.485, 0.35, 0.40, 0.01],
//                'Alien # for Permanent Residence': [0.747, 0.33, 0.216, 0.01],
//                'Alien # for Work Authorization': [0.833, 0.349, 0.13, 0.01],
//                'TranslatorAddress': [0.8, 0.48, 0.4, 0.01],
//                'TranslatorName': [0.52, 0.445, 0.25, 0.01],
//                'TranslatorDateOfSignature': [0.7, 0.48, 0.2, 0.01],
//                'List A - DocumentTitle': [0.12, 0.561, 0.215, 0.01],
//                'List A - IssuingAuthority': [0.13, 0.58, 0.2, 0.01],
//                'List A - DocumentNumber': [0.105, 0.605, 0.2, 0.01],
//                'List A - Expiration Date': [0.205, 0.62, 0.14, 0.01],
//                'List B - DocumentTitle': [0.385, 0.565, 0.2, 0.01],
//                'List B - IssuingAuthority': [0.385, 0.585, 0.2, 0.01],
//                'List B - DocumentNumber': [0.385, 0.605, 0.2, 0.01],
//                'List B - Expiration Date': [0.385, 0.625, 0.2, 0.01],
//                'List C - DocumentTitle': [0.725, 0.565, 0.2, 0.01],
//                'List C - IssuingAuthority': [0.725, 0.585, 0.2, 0.01],
//                'List C - DocumentNumber': [0.725, 0.605, 0.2, 0.01],
//                'List C - Expiration Date': [0.725, 0.625, 0.2, 0.01],
//                'List A - DocumentNumber - Second Section': [0.105, 0.64, 0.2, 0.01],
//                'List A - Expiration Date -  Second Section': [0.205, 0.66, 0.2, 0.01]
//        ]
//    }
//    if(version.contains('02/02/09') && pageNumber == 4) {
//        swapcoords = [
//                'LastName': [0.055, 0.180, 0.37, 0.204],
//                'FirstName': [0.368, 0.180, 0.61, 0.205],
//                'MiddleInitial': [0.610, 0.180, 0.686, 0.205],
//                'MaidenName': [0.69, 0.18, 0.94, 0.205],
//                'StreetAddress': [0.055, 0.217, 0.58, 0.240],
//                'City': [0.055, 0.252, 0.35, 0.275],
//                'DateOfBirth': [0.688, 0.217, 0.95, 0.240],
//                'SocialSecurity': [[0.688, 0.253, 0.95, 0.275]],
//                'State': [0.345, 0.252, 0.58, 0.275],
//                'Zip': [0.58, 0.252, 0.688, 0.275],
//                'Attestation': [0.49, 0.292, 0.515, 0.365],
//                'Alien # for Permanent Residence': [0.722, 0.325, 0.94, 0.345],
//                'Date Expiration of Work Authorization': [0.805, 0.362, 0.955, 0.377],
//                'Alien # for Work Authorization': [0.81, 0.346, 0.955, 0.365],
//                'TranslatorName': [0.513, 0.443, 0.94, 0.469],
//                'TranslatorAddress': [0.104, 0.482, 0.67, 0.505],
//                'TranslatorDateOfSignature': [0.68, 0.482, 0.94, 0.505],
//                'List A - DocumentTitle': [0.145, 0.564, 0.363, 0.586],
//                'List A - IssuingAuthority': [0.15, 0.586, 0.363, 0.605],
//                'List A - DocumentNumber': [0.126, 0.606, 0.363, 0.625],
//                'List A - DocumentExpirationDate': [0.215, 0.625, 0.363, 0.644],
//                'List A - DocumentTitle - Second Section': [],
//                'List A - IssuingAuthority - Second Section': [],
//                'List A - DocumentNumber - Second Section': [0.13, 0.644, 0.363, 0.662],
//                'List A - Document Expiration Date - Second Section': [0.215, 0.662, 0.363, 0.682],
//                'List B - DocumentTitle': [0.38, 0.561, 0.64, 0.585],
//                'List B - IssuingAuthority': [0.38, 0.585, 0.64, 0.605],
//                'List B - DocumentNumber': [0.38, 0.6052, 0.64, 0.6245],
//                'List B - DocumentExpirationDate': [0.38, 0.6245, 0.64, 0.6445],
//                'List C - DocumentTitle': [0.7, 0.561, 0.95, 0.585],
//                'List C - IssuingAuthority': [0.7, 0.585, 0.95, 0.605],
//                'List C - DocumentNumber': [0.7, 0.6052, 0.95, 0.6245],
//                'List C - DocumentExpirationDate': [0.7, 0.6245, 0.95, 0.6445],
//                'DateOfHire': [0.16, 0.711, 0.278, 0.726],
//                'Name of Employee Representative': [0.394, 0.752, 0.698, 0.777],
//                'Title': [0.698, 0.752, 0.95, 0.777],
//                'EmployerBusinessName': [0.05, 0.7875, 0.698, 0.808],
//                'Date Signed by Employer': [0.698, 0.7875, 0.95, 0.808]
//        ]
//    }
//    return swapcoords
//}
//
//def getDataPages(String version) {
//    page_info = [
//            '05/07/87': 0,
//            '11-21-91(L)': 0,
//            '11-21-91(R)': 2,
//            '05/31/05': 2,
//            '06/05/07': 3,
//            '02/02/09': 4,
//            '08/07/09': 0,
//            '03/08/13': [7, 8],
//            '11/14/2016': [1, 2],
//            '07/17/17': [1, 2]
//    ]
//    return page_info[version]
//}
//
//def getDataFromAcroForm(PDDocument document, stripper) {
//    def allPages = document.getDocumentCatalog().getPages()
//    def page = allPages.get(0)
//    stripper = new PDFTextStripperByArea()
//    def version = getFormVersion(page, stripper)
//    def fields = document.getDocumentCatalog().getAcroForm()
//
//    //if(version == blah blah handling if necessary)
//
//    def swapMap = [
//            'LastName': fields.getField("form1[0].#subform[3].lastname[0]").getValueAsString(),
//            'FirstName': fields.getField("form1[0].#subform[3].firstname[0]").getValueAsString(),
//            'MiddleInitial': fields.getField("form1[0].#subform[3].middleinitial[0]").getValueAsString(),
//            'MaidenName': fields.getField("form1[0].#subform[3].maidenname[0]").getValueAsString(),
//            'StreetAddress': fields.getField("form1[0].#subform[3].address[0]").getValueAsString(),
//            'ApartmentNo': fields.getField("form1[0].#subform[3].apartmentnumber[0]").getValueAsString(),
//            'City': fields.getField("form1[0].#subform[3].city[0]").getValueAsString(),
//            'State': fields.getField("form1[0].#subform[3].state[0]").getValueAsString(),
//            'Zip': fields.getField("form1[0].#subform[3].zipcode[0]").getValueAsString(),
//            'DateOfBirth': fields.getField("form1[0].#subform[3].dateofbirth[0]").getValueAsString(),
//            'SocialSecurity': fields.getField("form1[0].#subform[3].ssnum[0]").getValueAsString(),
//            'citizen': fields.getField("form1[0].#subform[3].citizen1[0]").isChecked(),
//            'national': fields.getField("form1[0].#subform[3].noncitizennational[0]").isChecked(),
//            'resident': fields.getField("form1[0].#subform[3].LPRAlienNumber[0]").isChecked(),
//            'alien': fields.getField("form1[0].#subform[3].alienauthorizedtowork[0]").isChecked(),
//            'Alien # for Permanent Residence': fields.getField("form1[0].#subform[3].LPRAlienNumber[1]").getValueAsString(),
//            'Alien # for Work Authorization': fields.getField("form1[0].#subform[3].alienworknumber[0]").getValueAsString(),
//            'TranslatorAddress': fields.getField("form1[0].#subform[3].preparersaddress[0]").getValueAsString(),
//            'TranslatorName': fields.getField("form1[0].#subform[3].printname[0]").getValueAsString(),
//            'TranslatorDateOfSignature': fields.getField("form1[0].#subform[3].preparerssignaturedate[0]").getValueAsString(),
//            'List A - DocumentTitle': fields.getField("form1[0].#subform[3].documenttitlelistA[0]").getValueAsString(),
//            'List A - IssuingAuthority': fields.getField("form1[0].#subform[3].issuingauthoritylistA[0]").getValueAsString(),
//            'List A - DocumentNumber': fields.getField("form1[0].#subform[3].docnumberlistA[0]").getValueAsString(),
//            'List A - Expiration Date': fields.getField("form1[0].#subform[3].expirationdatelistA[0]").getValueAsString(),
//            'List B - DocumentTitle': fields.getField("form1[0].#subform[3].listb1[0]").getValueAsString(),
//            'List B - IssuingAuthority': fields.getField("form1[0].#subform[3].listb2[0]").getValueAsString(),
//            'List B - DocumentNumber': fields.getField("form1[0].#subform[3].listb3[0]").getValueAsString(),
//            'List B - Expiration Date': fields.getField("form1[0].#subform[3].listb4[0]").getValueAsString(),
//            'List C - DocumentTitle': fields.getField("form1[0].#subform[3].listc1[0]").getValueAsString(),
//            'List C - IssuingAuthority': fields.getField("form1[0].#subform[3].listc2[0]").getValueAsString(),
//            'List C - DocumentNumber': fields.getField("form1[0].#subform[3].listc3[0]").getValueAsString(),
//            'List C - Expiration Date': fields.getField("form1[0].#subform[3].listc4[0]").getValueAsString(),
//            'List A - DocumentNumber - Second Section': fields.getField("form1[0].#subform[3].documentnumberlistA[0]").getValueAsString(),
//            'List A - Expiration Date -  Second Section': fields.getField("form1[0].#subform[3].expirationdate[0]").getValueAsString()
//    ]
//    return swapMap
//}
//
//def getDataFromBoxes(document, stripper) {
//    swapMap = [:]
//    allPages = document.getDocumentCatalog().getPages()
//    firstPage = allPages.get(0)
//    stripper = new PDFTextStripperByArea()
//
//    for (PDPage page : allPages) {
//        stripper = new PDFTextStripperByArea()
//        version = getFormVersion(page, stripper)
//        dataPages = getDataPages(version)
//        stripper = new PDFTextStripperByArea()
//        currentPage = getPageNumber(version, page, stripper)
//        if (version == 'Form version not found' || currentPage == 'Page number not found') {
//            print('version = ' + version + ' page number = ' + currentPage)
//            continue
//        }
//        for (int pageNumber : dataPages) {
//            if (currentPage != pageNumber)
//                continue
//            coords = getCoords(version, currentPage)
//            pheight = page.getMediaBox().getHeight()
//            pwidth = page.getMediaBox().getWidth()
//
//            // Reinitialize stripper to flush out the old coords for finding form version
//            stripper = new PDFTextStripperByArea()
//
//            // A better way to loop through the elements
//            def keys = coords.keySet()
//            for (String key : keys) {
//                if (coords[key] == null || coords[key].size() < 4)
//                    continue
//                def swapRectangle = new Rectangle(
//                        widthByPercent(coords[key][0]),
//                        heightByPercent(coords[key][1]),
//                        widthByPercent(coords[key][2]),
//                        heightByPercent(coords[key][3])
//                )
//                stripper.addRegion(key, swapRectangle)
//            }
//
//            //Load the results into a JSON
//            stripper.setSortByPosition(true)
//            stripper.extractRegions(page)
//            def regions = stripper.getRegions()
//            for (String region : regions) {
//                String box = stripper.getTextForRegion(region)
//                swapMap.put(region, box)
//            }
//        }
//    }
//    return swapMap
//}
//
////def flowFile = session.get()
////if(!flowFile) return
////
////flowFile = session.write(flowFile, { inputStream, outputStream ->
//try {
//    //Create objects
////    def inputStream = new File("nocr/jane_doe.pdf");
////        def inputStream = new File("ocr/testfiles/i-9_02-02-09.pdf");
//    def inputStream = new File("nocr/testfiles/ver07_james_bond.pdf");
//
//    def document = PDDocument.load(inputStream)
//    if(document.isEncrypted())
//        document.setAllSecurityToBeRemoved(true)
//
//    def boxMap = [:]
//    def stripper = new PDFTextStripperByArea()
//
//    // If document has an AcroForm that can be extracted, use that to fill in the JSON
////    if(document.getDocumentCatalog().getAcroForm().getFields().size() > 0) {
////        boxMap = getDataFromAcroForm(document, stripper)
////    }
////    else { // Fill in JSON by grabbing data from boxes
//        boxMap = getDataFromBoxes(document, stripper)
////    }
//
//    // Add the filename as an attribute
////        boxMap.put('File', flowFile.getAttribute('filename'))
//
//    // Convert the boxmap into a String to be passed through stdout
//    json = boxMap.inspect()
//    json = json.replace('\\n', '')
//    json = json.replace('\\r', '')
//    json = json.replace(',"', ',\n"')
//
////        outputStream.write(json.getBytes(StandardCharsets.UTF_8))
//    print("\n")
//    print(json)
//
//} catch (Exception e){
//    System.out.println(e.getMessage())
////        session.transfer(flowFile, REL_FAILURE)
//}
////} as StreamCallback)
////session.transfer(flowFile, REL_SUCCESS)
