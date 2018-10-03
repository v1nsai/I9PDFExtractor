import org.apache.pdfbox.pdmodel.PDDocument
import org.apache.pdfbox.text.PDFTextStripperByArea
import java.awt.Rectangle
import org.apache.pdfbox.pdmodel.PDPage
import java.nio.charset.StandardCharsets

pwidth = 0.00
pheight = 0.00

//Using percentages of page width and height is better at handling size variation than pixels
//These functions handle the conversion
def widthByPercent(double percent) {
    return (int)Math.round(percent * pwidth)
}

def heightByPercent(double percent) {
    return (int)Math.round(percent * pheight)
}

//Find the form version and load the JSON containing the proper coords
def getFormVersion(PDPage page, PDFTextStripperByArea stripper) {
    //Grab the top and bottom of the page, concatenate them and look for the Rev. date
    Rectangle formvertop = new Rectangle(widthByPercent(0), heightByPercent(0), widthByPercent(100), heightByPercent(8))
    stripper.addRegion("formvertop", formvertop)
    Rectangle formverbottom = new Rectangle(widthByPercent(0), heightByPercent(92), widthByPercent(100), heightByPercent(8))
    stripper.addRegion("formverbottom", formverbottom)
    stripper.setSortByPosition(true)
    stripper.extractRegions(page)
    List<String> regions = stripper.getRegions()
    String ver = ''
    for (String region : regions) {
        String swap = stripper.getTextForRegion(region)
        ver = ver + swap
    }
    if(ver.contains('(Rev. 02/02/09)')){
        return '02/02/09'
    }
    if(ver.contains('(Rev. 08/07/09)')){
        return '08/07/09'
    }
    if(ver.contains('03/08/13  N')){
        return '03/08/13'
    }
    if(ver.contains('11/14/2016 N')){
        return '11/14/16'
    }
    if(ver.contains('07/17/17  N')){
        return '07/17/17'
    }
}

def getCoords(String version, int pageNumber) {
    def swapcoords = [:]
    if(version.contains("08/07/09") && pageNumber == 4) {
        swapcoords = [
                'LastName': [0.0242, 0.1797, 0.2621, 0.02],
                'FirstName': [0.2984, 0.1797, 0.2931, 0.0219],
                'MiddleInitial': [0.6009, 0.1797, 0.0955, 0.0219],
                'MaidenName': [0.7057, 0.1816, 0.2595, 0.02],
                'StreetAddress': [0.0242, 0.2168, 0.535, 0.02],
                'ApartmentNo': [0.5673, 0.2177, 0.1277, 0.0191],
                'City': [0.0202, 0.251, 0.2931, 0.021],
                'State': [0.3213, 0.251, 0.2339, 0.0219],
                'Zip': [0.5619, 0.251, 0.1304, 0.02],
                'DateOfBirth': [0.7057, 0.2168, 0.2648, 0.02],
                'SocialSecurity': [0.703, 0.251, 0.2675, 0.0191],
//                'citizen': [0.4859, 0.29, 0.2142, 0.02],
//                'national': [0.4824, 0.311, 0.3612, 0.0119],
//                'resident': [0.48, 0.3291, 0.2271, 0.0137],
//                'alien': [0.4859, 0.3473, 0.2977, 0.0137],
                'Alien # for Permanent Residence': [0.746, 0.3213, 0.2245, 0.0162],
                'Alien # for Work Authorization': [0.8267, 0.3404, 0.1452, 0.0134],
                'TranslatorAddress': [0.0632, 0.4715, 0.6197, 0.0238],
                'TranslatorName': [0.5162, 0.4354, 0.4127, 0.0238],
                'TranslatorDateOfSignature': [0.6923, 0.4734, 0.2595, 0.02],
                'List A - DocumentTitle': [0.1483, 0.5637, 0.2024, 0.0164],
                'List A - IssuingAuthority': [0.153, 0.591, 0.1989, 0.0119],
                'List A - DocumentNumber': [0.1306, 0.6064, 0.2165, 0.0155],
                'List A - Expiration Date': [0.2177, 0.6273, 0.1318, 0.0137],
                'List B - DocumentTitle': [0.3818, 0.558, 0.2393, 0.0153],
                'List B - IssuingAuthority': [0.3848, 0.5882, 0.2377, 0.0146],
                'List B - DocumentNumber': [0.3848, 0.6082, 0.2365, 0.0146],
                'List B - Expiration Date': [0.3871, 0.6273, 0.2342, 0.0164],
                'List C - DocumentTitle': [0.7059, 0.5646, 0.2318, 0.0182],
                'List C - IssuingAuthority': [0.7036, 0.5882, 0.2365, 0.0146],
                'List C - DocumentNumber': [0.7024, 0.6055, 0.2436, 0.0164],
                'List C - Expiration Date': [0.7, 0.6264, 0.2412, 0.0173],
                'List A - DocumentNumber - Second Section': [0.1306, 0.6437, 0.2224, 0.0164],
                'List A - Expiration Date -  Second Section': [0.2177, 0.6673, 0.133, 0.0119]
        ]
    }
    if(version.contains('02/02/09') && pageNumber == 4) {
        swapcoords = [
                'LastName': [0.0483, 0.181, 0.2048, 0.0228],
                'FirstName': [0.2942, 0.181, 0.2883, 0.0228],
                'MiddleInitial': [0.5942, 0.1837, 0.0883, 0.0164],
                'MaidenName': [0.6906, 0.18, 0.2542, 0.021],
                'StreetAddress': [0.0518, 0.2191, 0.4624, 0.0173],
                'ApartmentNo': [0.5377, 0.22, 0.1412, 0.0146],
                'City': [0.0518, 0.2546, 0.2083, 0.0173],
                'State': [0.2624, 0.2519, 0.2648, 0.0219],
                'Zip': [0.5495, 0.251, 0.133, 0.02],
                'DateOfBirth': [0.6906, 0.22, 0.2565, 0.0155],
                'SocialSecurity': [0.6906, 0.2555, 0.2518, 0.0182],
//                'citizen': [0.4859, 0.29, 0.2142, 0.02],
//                'national': [0.4824, 0.311, 0.3612, 0.0119],
//                'resident': [0.48, 0.3291, 0.2271, 0.0137],
//                'alien': [0.4859, 0.3473, 0.2977, 0.0137],
                'Alien # for Permanent Residence': [0.7259, 0.3282, 0.2153, 0.0137],
                'Alien # for Work Authorization': [0.8048, 0.3473, 0.1318, 0.011],
                'TranslatorAddress': [0.0753, 0.4791, 0.5953, 0.0246],
                'TranslatorName': [0.5142, 0.4437, 0.3777, 0.0228],
                'TranslatorDateOfSignature': [0.68, 0.4828, 0.2636, 0.0182],
                'List A - DocumentTitle': [0.1483, 0.5637, 0.2024, 0.0164],
                'List A - IssuingAuthority': [0.153, 0.591, 0.1989, 0.0119],
                'List A - DocumentNumber': [0.1306, 0.6064, 0.2165, 0.0155],
                'List A - Expiration Date': [0.2177, 0.6273, 0.1318, 0.0137],
                'List B - DocumentTitle': [0.3883, 0.5619, 0.2365, 0.0219],
                'List B - IssuingAuthority': [0.3848, 0.5882, 0.2377, 0.0146],
                'List B - DocumentNumber': [0.3848, 0.6082, 0.2365, 0.0146],
                'List B - Expiration Date': [0.3871, 0.6273, 0.2342, 0.0164],
                'List C - DocumentTitle': [0.7059, 0.5646, 0.2318, 0.0182],
                'List C - IssuingAuthority': [0.7036, 0.5882, 0.2365, 0.0146],
                'List C - DocumentNumber': [0.7024, 0.6055, 0.2436, 0.0164],
                'List C - Expiration Date': [0.7, 0.6264, 0.2412, 0.0173],
                'List A - DocumentNumber - Second Section': [0.1306, 0.6437, 0.2224, 0.0164],
                'List A - Expiration Date -  Second Section': [0.2177, 0.6673, 0.133, 0.0119]
        ]
    }
    if(version.contains('03/08/13') && pageNumber == 7) {
        swapcoords = [
                'LastName': [0.0589, 0.2243, 0.2118, 0.0223],
                'FirstName': [0.2733, 0.2233, 0.2837, 0.0223],
                'MiddleInitial': [0.5595, 0.2243, 0.102, 0.0203],
                'MaidenName': [0.6667, 0.2243, 0.2759, 0.0223],
                'StreetAddress': [0.0589, 0.2627, 0.3334, 0.0203],
                'ApartmentNo': [0.3987, 0.2617, 0.0916, 0.0203],
                'City': [0.4994, 0.2637, 0.2249, 0.0182],
                'State': [0.7334, 0.2627, 0.0654, 0.0223],
                'Zip': [0.8066, 0.2627, 0.1347, 0.0223],
                'DateOfBirth': [0.0628, 0.3021, 0.1648, 0.0223],
                'SocialSecurity': [0.2327, 0.3031, 0.17, 0.0233],
                'EmailAddress': [0.4105, 0.3041, 0.3386, 0.0213],
                'PhoneNumber': [0.7582, 0.3041, 0.1804, 0.0213],
//                'citizen': [0.0523, 0.3839, 0.051, 0.0192],
//                'national': [0.051, 0.4051, 0.0367, 0.0223],
//                'resident': [0.051, 0.4293, 0.0327, 0.0182],
//                'alien': [0.051, 0.4495, 0.0314, 0.0233],
                'Alien # for Permanent Residence': [0.5648, 0.4273, 0.221, 0.0152],
                'Alien # for Work Authorization': [0.3831, 0.5061, 0.2144, 0.0192],
                'Form I-94 Admission Number': [0.302, 0.5415, 0.2902, 0.0213],

                //'PassportNumber': //this needs to be added,
                //'PassportCountry': //so does this

                'TranslatorAddress': [0.0589, 0.894, 0.8863, 0.0223],
                'TranslatorName': [0.0589, 0.8596, 0.8824, 0.0182],
                'TranslatorDateOfSignature': [0.753, 0.8213, 0.1883, 0.0213]
        ]
    }
    if(version.contains('03/08/13') && pageNumber == 8) {
        swapcoords = [
                'List A - DocumentTitle': [0.0576, 0.2061, 0.2824, 0.0132],
                'List A - IssuingAuthority': [0.0589, 0.2334, 0.2811, 0.0132],
                'List A - DocumentNumber': [0.0602, 0.2607, 0.2798, 0.0122],
                'List A - Expiration Date': [0.0602, 0.2879, 0.2798, 0.0182],
                'List B - DocumentTitle': [0.3556, 0.2051, 0.2902, 0.0162],
                'List B - IssuingAuthority': [0.3556, 0.2324, 0.2863, 0.0152],
                'List B - DocumentNumber': [0.3556, 0.2607, 0.2863, 0.0152],
                'List B - Expiration Date': [0.3556, 0.2879, 0.2863, 0.0162],
                'List C - DocumentTitle': [0.6536, 0.2051, 0.2824, 0.0152],
                'List C - IssuingAuthority': [0.6523, 0.2314, 0.2863, 0.0142],
                'List C - DocumentNumber': [0.6523, 0.2596, 0.2876, 0.0162],
                'List C - Expiration Date': [0.6536, 0.2879, 0.2824, 0.0182],
                'List A - DocumentNumber - Second Section': [0.0576, 0.3728, 0.2824, 0.01],
                'List A - Expiration Date -  Second Section': [0.0589, 0.4, 0.2811, 0.0142]
        ]
    }
    if(version.contains('11/14/16') && pageNumber == 1){
        swapcoords = [
                'LastName': [0.0589, 0.2445, 0.2733, 0.0182],
                'FirstName': [0.3399, 0.2425, 0.2393, 0.0213],
                'MiddleInitial': [0.5909, 0.2435, 0.0929, 0.0182],
                'MaidenName': [0.6929, 0.2435, 0.2432, 0.0162],
                'StreetAddress': [0.0628, 0.2819, 0.3229, 0.0162],
                'ApartmentNo': [0.3974, 0.2819, 0.085, 0.0182],
                'City': [0.4981, 0.2819, 0.238, 0.0172],
                'State': [0.7438, 0.2768, 0.0523, 0.0213],
                'Zip': [0.8027, 0.2778, 0.1347, 0.0213],
                'DateOfBirth': [0.0602, 0.3182, 0.1739, 0.0253],
                'SocialSecurity': [0.2458, 0.3172, 0.1883, 0.0263],
                'EmailAddress': [0.4432, 0.3203, 0.2719, 0.0223],
                'PhoneNumber': [0.7255, 0.3172, 0.2118, 0.0243],
//                'citizen': [0.4859, 0.29, 0.2142, 0.02],
//                'national': [0.4824, 0.311, 0.3612, 0.0119],
//                'resident': [0.48, 0.3291, 0.2271, 0.0137],
//                'alien': [0.4859, 0.3473, 0.2977, 0.0137],
                'Alien # for Permanent Residence': [0.5726, 0.4526, 0.2014, 0.0152],
                'Alien # for Work Authorization': [0.3687, 0.5344, 0.2249, 0.0253],
                'Form I-94 Admission Number': [0.285, 0.5718, 0.3085, 0.0192],
                'PassportNumber': [0.2654, 0.598, 0.3268, 0.0223],
                'PassportCountry':[0.2327, 0.6253, 0.3582, 0.0182],
                'TranslatorAddress': [0.0615, 0.8647, 0.8785, 0.0182],
                'TranslatorName': [0.0615, 0.8273, 0.8746, 0.0162],
                'TranslatorDateOfSignature': [0.6811, 0.7899, 0.2563, 0.0182]
        ]
    }
    if(version.contains('11/14/16') && pageNumber == 2) {
        swapcoords = [
                'List A - DocumentTitle': [0.0602, 0.2314, 0.2785, 0.0142],
                'List A - IssuingAuthority': [0.0615, 0.2617, 0.2811, 0.0132],
                'List A - DocumentNumber': [0.0602, 0.2899, 0.2785, 0.0112],
                'List A - Expiration Date': [0.0641, 0.3182, 0.2746, 0.0152],
                'List B - DocumentTitle': [0.3608, 0.2304, 0.2811, 0.0192],
                'List B - IssuingAuthority': [0.3582, 0.2617, 0.2863, 0.0132],
                'List B - DocumentNumber': [0.3582, 0.2879, 0.2863, 0.0172],
                'List B - Expiration Date': [0.3608, 0.3172, 0.2811, 0.0162],
                'List C - DocumentTitle': [0.6563, 0.2304, 0.2824, 0.0172],
                'List C - IssuingAuthority': [0.6536, 0.2627, 0.2889, 0.0122],
                'List C - DocumentNumber': [0.6589, 0.2889, 0.2811, 0.0142],
                'List C - Expiration Date': [0.6602, 0.3192, 0.2785, 0.0152],
                'List A - DocumentNumber - Second Section': [0.0615, 0.4071, 0.2811, 0.0132],
                'List A - Expiration Date -  Second Section': [0.0615, 0.4324, 0.2785, 0.0162]
        ]
    }
    if(version.contains('07/17/17') && pageNumber == 1){
        swapcoords = [
                'LastName': [0.0589, 0.2445, 0.2733, 0.0182],
                'FirstName': [0.3399, 0.2425, 0.2393, 0.0213],
                'MiddleInitial': [0.5909, 0.2435, 0.0929, 0.0182],
                'MaidenName': [0.6929, 0.2435, 0.2432, 0.0162],
                'StreetAddress': [0.0628, 0.2819, 0.3229, 0.0162],
                'ApartmentNo': [0.3974, 0.2819, 0.085, 0.0182],
                'City': [0.4981, 0.2819, 0.238, 0.0172],
                'State': [0.7438, 0.2768, 0.0523, 0.0213],
                'Zip': [0.8027, 0.2778, 0.1347, 0.0213],
                'DateOfBirth': [0.0602, 0.3182, 0.1739, 0.0253],
                'SocialSecurity': [0.2458, 0.3172, 0.1883, 0.0263],
                'EmailAddress': [0.4432, 0.3203, 0.2719, 0.0223],
                'PhoneNumber': [0.7255, 0.3172, 0.2118, 0.0243],
//                'citizen': [0.4859, 0.29, 0.2142, 0.02],
//                'national': [0.4824, 0.311, 0.3612, 0.0119],
//                'resident': [0.48, 0.3291, 0.2271, 0.0137],
//                'alien': [0.4859, 0.3473, 0.2977, 0.0137],
                'Alien # for Permanent Residence': [0.5726, 0.4526, 0.2014, 0.0152],
                'Alien # for Work Authorization': [0.3687, 0.5344, 0.2249, 0.0253],
                'Form I-94 Admission Number': [0.285, 0.5718, 0.3085, 0.0192],
                'PassportNumber': [0.2654, 0.598, 0.3268, 0.0223],
                'PassportCountry':[0.2327, 0.6253, 0.3582, 0.0182],
                'TranslatorAddress': [0.0615, 0.8647, 0.8785, 0.0182],
                'TranslatorName': [0.0615, 0.8273, 0.8746, 0.0162],
                'TranslatorDateOfSignature': [0.6811, 0.7899, 0.2563, 0.0182]
        ]
    }
    if(version.contains('07/17/17') && pageNumber == 2) {
        swapcoords = [
                'List A - DocumentTitle': [0.0602, 0.2314, 0.2785, 0.0142],
                'List A - IssuingAuthority': [0.0615, 0.2617, 0.2811, 0.0132],
                'List A - DocumentNumber': [0.0602, 0.2899, 0.2785, 0.0112],
                'List A - Expiration Date': [0.0641, 0.3182, 0.2746, 0.0152],
                'List B - DocumentTitle': [0.3608, 0.2304, 0.2811, 0.0192],
                'List B - IssuingAuthority': [0.3582, 0.2617, 0.2863, 0.0132],
                'List B - DocumentNumber': [0.3582, 0.2879, 0.2863, 0.0172],
                'List B - Expiration Date': [0.3608, 0.3172, 0.2811, 0.0162],
                'List C - DocumentTitle': [0.6563, 0.2304, 0.2824, 0.0172],
                'List C - IssuingAuthority': [0.6536, 0.2627, 0.2889, 0.0122],
                'List C - DocumentNumber': [0.6589, 0.2889, 0.2811, 0.0142],
                'List C - Expiration Date': [0.6602, 0.3192, 0.2785, 0.0152],
                'List A - DocumentNumber - Second Section': [0.0615, 0.4071, 0.2811, 0.0132],
                'List A - Expiration Date -  Second Section': [0.0615, 0.4324, 0.2785, 0.0162]
        ]
    }
    return swapcoords
}

def getDataPages(String version) {
    page_info = [
            '05/07/87': 0,
            '11-21-91(L)': 0,
            '11-21-91(R)': 2,
            '05/31/05': 2,
            '06/05/07': 3,
            '02/02/09': 4,
            '08/07/09': 4,
            '03/08/13': [7, 8],
            '11/14/16': [1, 2],
            '07/17/17': [1, 2]
    ]
    return page_info[version]
}

def getDataFromAcroForm(PDDocument document, String version) {
    def fields = document.getDocumentCatalog().getAcroForm()
    def swapMap = [:]
    if(version == '08/07/09') {
        swapMap = [
            'LastName': fields.getField("form1[0].#subform[3].lastname[0]").getValueAsString(),
            'FirstName': fields.getField("form1[0].#subform[3].firstname[0]").getValueAsString(),
            'MiddleInitial': fields.getField("form1[0].#subform[3].middleinitial[0]").getValueAsString(),
            'MaidenName': fields.getField("form1[0].#subform[3].maidenname[0]").getValueAsString(),
            'StreetAddress': fields.getField("form1[0].#subform[3].address[0]").getValueAsString(),
            'ApartmentNo': fields.getField("form1[0].#subform[3].apartmentnumber[0]").getValueAsString(),
            'City': fields.getField("form1[0].#subform[3].city[0]").getValueAsString(),
            'State': fields.getField("form1[0].#subform[3].state[0]").getValueAsString(),
            'Zip': fields.getField("form1[0].#subform[3].zipcode[0]").getValueAsString(),
            'DateOfBirth': fields.getField("form1[0].#subform[3].dateofbirth[0]").getValueAsString(),
            'SocialSecurity': fields.getField("form1[0].#subform[3].ssnum[0]").getValueAsString(),
//            'citizen': fields.getField("form1[0].#subform[3].citizen1[0]").isChecked(),
//            'national': fields.getField("form1[0].#subform[3].noncitizennational[0]").isChecked(),
//            'resident': fields.getField("form1[0].#subform[3].LPRAlienNumber[0]").isChecked(),
//            'alien': fields.getField("form1[0].#subform[3].alienauthorizedtowork[0]").isChecked(),
            'Alien # for Permanent Residence': fields.getField("form1[0].#subform[3].LPRAlienNumber[1]").getValueAsString(),
            'Alien # for Work Authorization': fields.getField("form1[0].#subform[3].alienworknumber[0]").getValueAsString(),
            'TranslatorAddress': fields.getField("form1[0].#subform[3].preparersaddress[0]").getValueAsString(),
            'TranslatorName': fields.getField("form1[0].#subform[3].printname[0]").getValueAsString(),
            'TranslatorDateOfSignature': fields.getField("form1[0].#subform[3].preparerssignaturedate[0]").getValueAsString(),
            'List A - DocumentTitle': fields.getField("form1[0].#subform[3].documenttitlelistA[0]").getValueAsString(),
            'List A - IssuingAuthority': fields.getField("form1[0].#subform[3].issuingauthoritylistA[0]").getValueAsString(),
            'List A - DocumentNumber': fields.getField("form1[0].#subform[3].docnumberlistA[0]").getValueAsString(),
            'List A - Expiration Date': fields.getField("form1[0].#subform[3].expirationdatelistA[0]").getValueAsString(),
            'List B - DocumentTitle': fields.getField("form1[0].#subform[3].listb1[0]").getValueAsString(),
            'List B - IssuingAuthority': fields.getField("form1[0].#subform[3].listb2[0]").getValueAsString(),
            'List B - DocumentNumber': fields.getField("form1[0].#subform[3].listb3[0]").getValueAsString(),
            'List B - Expiration Date': fields.getField("form1[0].#subform[3].listb4[0]").getValueAsString(),
            'List C - DocumentTitle': fields.getField("form1[0].#subform[3].listc1[0]").getValueAsString(),
            'List C - IssuingAuthority': fields.getField("form1[0].#subform[3].listc2[0]").getValueAsString(),
            'List C - DocumentNumber': fields.getField("form1[0].#subform[3].listc3[0]").getValueAsString(),
            'List C - Expiration Date': fields.getField("form1[0].#subform[3].listc4[0]").getValueAsString(),
            'List A - DocumentNumber - Second Section': fields.getField("form1[0].#subform[3].documentnumberlistA[0]").getValueAsString(),
            'List A - Expiration Date -  Second Section': fields.getField("form1[0].#subform[3].expirationdate[0]").getValueAsString()
        ]
    }
    if(version == '02/02/09') {
        swapMap = [
                'LastName': fields.getField("form1[0].#subform[3].lastname[0]").getValueAsString(),
                'FirstName': fields.getField("form1[0].#subform[3].firstname[0]").getValueAsString(),
                'MiddleInitial': fields.getField("form1[0].#subform[3].middlename[0]").getValueAsString(),
                'MaidenName': fields.getField("form1[0].#subform[3].maidenname[0]").getValueAsString(),
                'StreetAddress': fields.getField("form1[0].#subform[3].address[0]").getValueAsString(),
                'ApartmentNo': fields.getField("form1[0].#subform[3].apartmentnumber[0]").getValueAsString(),
                'City': fields.getField("form1[0].#subform[3].city[0]").getValueAsString(),
                'State': fields.getField("form1[0].#subform[3].state[0]").getValueAsString(),
                'Zip': fields.getField("form1[0].#subform[3].zipcode[0]").getValueAsString(),
                'DateOfBirth': fields.getField("form1[0].#subform[3].dateofbirth[0]").getValueAsString(),
                'SocialSecurity': fields.getField("form1[0].#subform[3].ssnum[0]").getValueAsString(),
                'citizen': fields.getField("form1[0].#subform[3].citizen1[0]").isChecked(),
                'national': fields.getField("form1[0].#subform[3].alienauthorizeds1[0]").isChecked(),
                'resident': fields.getField("form1[0].#subform[3].lawfulperm1[0]").isChecked(),
                'alien': fields.getField("form1[0].#subform[3].alienauthorizeds1[1]").isChecked(),
                'Alien # for Permanent Residence': fields.getField("form1[0].#subform[3].TextField1[0]").getValueAsString(),
                'Alien # for Work Authorization': fields.getField("form1[0].#subform[3].TextField1[1]").getValueAsString(),
                'TranslatorAddress': fields.getField("form1[0].#subform[3].address2[0]").getValueAsString(),
                'TranslatorName': fields.getField("form1[0].#subform[3].printname[0]").getValueAsString(),
                'TranslatorDateOfSignature': fields.getField("form1[0].#subform[3].middledate[0]").getValueAsString(),
                'List A - DocumentTitle': fields.getField("form1[0].#subform[3].documanttitle[0]").getValueAsString(),
                'List A - IssuingAuthority': fields.getField("form1[0].#subform[3].issuing_authority[0]").getValueAsString(),
                'List A - DocumentNumber': fields.getField("form1[0].#subform[3].docnumber[0]").getValueAsString(),
                'List A - Expiration Date': fields.getField("form1[0].#subform[3].expirationdate[0]").getValueAsString(),
                'List B - DocumentTitle': fields.getField("form1[0].#subform[3].listb1[0]").getValueAsString(),
                'List B - IssuingAuthority': fields.getField("form1[0].#subform[3].listb2[0]").getValueAsString(),
                'List B - DocumentNumber': fields.getField("form1[0].#subform[3].listb3[0]").getValueAsString(),
                'List B - Expiration Date': fields.getField("form1[0].#subform[3].listb4[0]").getValueAsString(),
                'List C - DocumentTitle': fields.getField("form1[0].#subform[3].listb1[1]").getValueAsString(),
                'List C - IssuingAuthority': fields.getField("form1[0].#subform[3].listb2[1]").getValueAsString(),
                'List C - DocumentNumber': fields.getField("form1[0].#subform[3].listb3[1]").getValueAsString(),
                'List C - Expiration Date': fields.getField("form1[0].#subform[3].listb4[1]").getValueAsString(),
                'List A - DocumentNumber - Second Section': fields.getField("form1[0].#subform[3].documanrt2[0]").getValueAsString(),
                'List A - Expiration Date -  Second Section': fields.getField("form1[0].#subform[3].expirationdate2[0]").getValueAsString()
        ]
    }
    if(version == '03/08/13') {
        swapMap = [
                'LastName': fields.getField("form1[0].#subform[6].FamilyName[0]").getValueAsString(),
                'FirstName': fields.getField("form1[0].#subform[6].GivenName[0]").getValueAsString(),
                'MiddleInitial': fields.getField("form1[0].#subform[6].MiddleInitial[0]").getValueAsString(),
                'MaidenName': fields.getField("form1[0].#subform[6].OtherNamesUsed[0]").getValueAsString(),
                'StreetAddress': fields.getField("form1[0].#subform[6].StreetNumberName[0]").getValueAsString(),
                'ApartmentNo': fields.getField("form1[0].#subform[6].AptNumber[0]").getValueAsString(),
                'City': fields.getField("form1[0].#subform[6].CityOrTown[0]").getValueAsString(),
                'State': fields.getField("form1[0].#subform[6].State[0]").getValueAsString(),
                'Zip': fields.getField("form1[0].#subform[6].ZipCode[0]").getValueAsString(),
                'DateOfBirth': fields.getField("form1[0].#subform[6].DateOfBirth[0]").getValueAsString(),
                'SocialSecurity': fields.getField("form1[0].#subform[6].SocialSecurityNumber1[0]").getValueAsString() + ' ' +
                        fields.getField("form1[0].#subform[6].SocialSecurityNumber2[0]").getValueAsString() + ' ' +
                        fields.getField("form1[0].#subform[6].SocialSecurityNumber3[0]").getValueAsString(),
                'citizen': fields.getField("form1[0].#subform[6].Checkbox1a[0]").isChecked(),
                'national': fields.getField("form1[0].#subform[6].Checkbox1b[0]").isChecked(),
                'resident': fields.getField("form1[0].#subform[6].Checkbox1c[0]").isChecked(),
                'alien': fields.getField("form1[0].#subform[6].Checkbox1d[0]").isChecked(),
                'Alien # for Permanent Residence': fields.getField("form1[0].#subform[6].AlienNumber[0]").getValueAsString(),
                'Alien # for Work Authorization': fields.getField("form1[0].#subform[6].AlienNumber[1]").getValueAsString(),
                'TranslatorAddress': fields.getField("form1[0].#subform[6].StreetNumberName[1]").getValueAsString() + ' ' +
                        fields.getField("form1[0].#subform[6].CityOrTown[1]").getValueAsString() + ' ' +
                        fields.getField("form1[0].#subform[6].State_Preparer[0]").getValueAsString() + ' ' +
                        fields.getField("form1[0].#subform[6].ZipCode[1]").getValueAsString(),
                'TranslatorName': fields.getField("form1[0].#subform[6].FirstName[0]").getValueAsString() + ' ' +
                        fields.getField("form1[0].#subform[6].LastName[0]").getValueAsString(),
                'TranslatorDateOfSignature': fields.getField("form1[0].#subform[6].DateofSignature[0]").getValueAsString(),
                //Page 7
                'List A - DocumentTitle': fields.getField("form1[0].#subform[7].ListA_DocumentTitle[0]").getValueAsString(),
                'List A - IssuingAuthority': fields.getField("form1[0].#subform[7].ListB_IssuingAuthority[1]").getValueAsString(),
                'List A - DocumentNumber': fields.getField("form1[0].#subform[7].ListADocumentNumber1[1]").getValueAsString(),
                'List A - Expiration Date': fields.getField("form1[0].#subform[7].ListAExpirationDate_1[0]").getValueAsString(),
                'List B - DocumentTitle': fields.getField("form1[0].#subform[7].ListB_DocumentTitle[0]").getValueAsString(),
                'List B - IssuingAuthority': fields.getField("form1[0].#subform[7].ListB_IssuingAuthority[0]").getValueAsString(),
                'List B - DocumentNumber': fields.getField("form1[0].#subform[7].ListBDocumentNumber1[0]").getValueAsString(),
                'List B - Expiration Date': fields.getField("form1[0].#subform[7].ListBExpirationDate[0]").getValueAsString(),
                'List C - DocumentTitle': fields.getField("form1[0].#subform[7].ListC_DocumentTitle[0]").getValueAsString(),
                'List C - IssuingAuthority': fields.getField("form1[0].#subform[7].ListC_IssuingAuthority[0]").getValueAsString(),
                'List C - DocumentNumber': fields.getField("form1[0].#subform[7].ListC_DocumentNumber1[0]").getValueAsString(),
                'List C - Expiration Date': fields.getField("form1[0].#subform[7].ListC_ExpirationDate[0]").getValueAsString(),
                'List A - DocumentNumber - Second Section': fields.getField("form1[0].#subform[7].ListADocumentNumber1[4]").getValueAsString(),
                'List A - Expiration Date -  Second Section': fields.getField("form1[0].#subform[7].ListAExpirationDate_2[0]").getValueAsString()
        ]
    }
    return swapMap
}

def getDataFromBoxes(version, dataPages, allPages) {
    def boxMap = [:]
    def pageCount = allPages.getCount()
    def blankPages = 0

    stripper = new PDFTextStripperByArea()
    // For each page, get page number, version, dimensions, set relevant coords and extract
    for(PDPage page : allPages) {
        this.pheight = page.getMediaBox().getHeight()
        this.pwidth = page.getMediaBox().getWidth()
        version = getFormVersion(page, stripper)
        currentPage = getPageNumber(version, page, stripper)
        if(version == 'Form version not found' || currentPage == 'Page number not found') {
            blankPages += 1
            continue
        }
        // If page number is not one of the pages that contains data, skip
        for (int pageNumber : dataPages) {
            if(currentPage != pageNumber) {
                continue
            }
            coords = getCoords(version, currentPage)
            pheight = page.getMediaBox().getHeight()
            pwidth = page.getMediaBox().getWidth()

            // Reinitialize stripper to flush out the old coords for finding form version
            stripper = new PDFTextStripperByArea()

            // A better way to loop through the elements
            def keys = coords.keySet()
            for (String key : keys) {
                if (coords[key] == null || coords[key].size() < 4)
                    continue
                def swapRectangle = new Rectangle(
                        widthByPercent(coords[key][0]),
                        heightByPercent(coords[key][1]),
                        widthByPercent(coords[key][2]),
                        heightByPercent(coords[key][3])
                )
                stripper.addRegion(key, swapRectangle)
            }

            //Load the results into a JSON
            stripper.setSortByPosition(true)
            stripper.extractRegions(page)
            regions = stripper.getRegions()
            for (String region : regions) {
                String box = stripper.getTextForRegion(region)
                boxMap.put(region, box)
            }
            boxMap.put('form_number', version)
        }
    }
    // Make sure form was readable at all by checking for blank output
    if(pageCount == blankPages)
        throw new Exception('No data, form or page number not readable')

    return boxMap
}

def getPageNumber(version, page, stripper) {
    //Grab the top and bottom of the page, concatenate them and look for the Rev. date
    Rectangle formvertop = new Rectangle(widthByPercent(0), heightByPercent(0), widthByPercent(100), heightByPercent(8))
    stripper.addRegion("formvertop", formvertop)
    Rectangle formverbottom = new Rectangle(widthByPercent(0), heightByPercent(92), widthByPercent(100), heightByPercent(8))
    stripper.addRegion("formverbottom", formverbottom)
    stripper.setSortByPosition(true)
    stripper.extractRegions(page)
    List<String> regions = stripper.getRegions()
    String ver = ''
    for (String region : regions) {
        String swap = stripper.getTextForRegion(region)
        ver = ver + swap
    }
    def m = ver =~ /(Page \d)/
    if (m) {
        page = m.group().replace("Page ", "")
        return Integer.parseInt(page)
    }
    else
        return 'Page number not found'
}

def flowFile = session.get()
if(!flowFile) return

flowFile = session.write(flowFile, { inputStream, outputStream ->
    try {
        // Test files to emulate flowFiles for testing
        // def inputStream = new File("nocr/testfiles/ver07_jane_doe.pdf");
        // def inputStream = new File("ocr/testfiles/i-9_02-02-09.pdf");
        // def inputStream = new File("nocr/testfiles/ver07_james_bond.pdf");
        // def inputStream = new File("nocr/marvin_decrypted.pdf")

        def document = PDDocument.load(inputStream)
        if(document.isEncrypted())
            document.setAllSecurityToBeRemoved(true)

        def stripper = new PDFTextStripperByArea()

        //Get the first page
        def allPages = document.getDocumentCatalog().getPages()
        def page = allPages.get(0)

        // getDataFromBoxes breaks without this being here, may not be properly setting global vars
        pheight = page.getMediaBox().getHeight()
        pwidth = page.getMediaBox().getWidth()

        // Get version and pages containing data using the first page
        def version = getFormVersion(page, stripper)
        def dataPages = getDataPages(version)
        def coords = [:]
        def boxMap = [:]

//        document.getDocumentCatalog().getAcroForm().flatten()
        // If document has an AcroForm that can be extracted, use that to fill in the JSON
        if(document.getDocumentCatalog().getAcroForm()) {
            // Some PDFs return an AcroForm even though they have 0 fields.  Can't call this first because it throws an exception on a null object.....
            if(document.getDocumentCatalog().getAcroForm().getFields().size() == 0) {
                boxMap = getDataFromBoxes(version, dataPages, allPages)
            }else {
                boxMap = getDataFromAcroForm(document, version)
            }
        } else {
            boxMap = getDataFromBoxes(version, dataPages, allPages)
        }

        // Add up the length of all key values to make sure the data was able to be extracted
        // Using a nonzero length to account for mistakenly reading form prompots
        def keys = boxMap.keySet()
        def mapSize = 0
        for(String key : keys) {
            mapSize += boxMap[key].size()
        }
        if(mapSize < 15)
            throw new Exception('Unable to read form filled data')

        // Add the filename as an attribute
        fileName = flowFile.getAttribute('filename')
        boxMap.put('File', fileName)

        // Add the pipeline as an attribute
        boxMap.put('Pipeline', 'nOCR')

        // Add box, sub-box and page # to output
//        def m = fileName =~ /SB(\d) (\d+)/
//        if(m)
//            subBox = m.group(1)
//            boxPage = m.group(2)
//
//        // Box will just have to be hard coded
//        boxMap.put('Box', 1)
//        boxMap.put('Sub-box', subBox)
//        boxMap.put('BoxPage', boxPage)

        // Convert the boxmap into a String to be passed through stdout
        json = boxMap.inspect()
        json = json.replace('\\n', '')
        json = json.replace('\\r', '')
        json = json.replace(',"', ',\n"')
        json = json.replace('\'', '"')
        json = json.replace('[', '{')
        json = json.replace(']', '}')

        outputStream.write(json.getBytes(StandardCharsets.UTF_8))
//        print("\n")
//        print(json)

    } catch (Exception e){
        System.out.println(e.getMessage())
        session.transfer(flowFile, REL_FAILURE)
    }
} as StreamCallback)
session.transfer(flowFile, REL_SUCCESS)