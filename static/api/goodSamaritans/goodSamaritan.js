var protocol = window.location.protocol
var hostUrl = protocol + "//" + window.location.host + "/"
var url = window.location.href
let subUrl = url.split("/")
var goodSamaritanid = parseInt(subUrl[4])
$(() => {
    goodSamaritan();
})

// const calculateAge = (dateOfBirth) => {
//     const today = new Date();
//     const diffInMilliseconds = today - dateOfBirth;
//     const diffInYears = diffInMilliseconds / (1000 * 60 * 60 * 24 * 365.25);
//     return Math.floor(diffInYears);
// }

const checkBoolean = (boolean) => {
    if(boolean == true){
        return "Yes"
    } else if(boolean==false){
        return "No"
    }
}

const goodSamaritan = () =>{
    // $("#spinner-container").show();
    var auth_user_token = $("#auth-user-token").val();

    $.ajax({
        "url": `${hostUrl}api/en/scgmp/good-samaritan/${goodSamaritanid}`,
        "method": "GET",
        "headers": {
            "Authorization": `Token ${ auth_user_token }`
        },
        onerror: (error) => {
            $("#spinner-container").hide();
            console.log(error.responseText);
        }
    }).done((response) => {
        // console.log(response)
        var DoB = new Date(response.BirthDate)
        // var age = calculateAge(DoB)
        // console.log(age)
        var dateToFormat = new Date(response.created)
        var dobToFormat = new Date(response.BirthDate)
        var currencyFormat = new Intl.NumberFormat("en-UG", {style: "currency", currency: "UGX", decimal: 3}).format(response.howMuch)
        // var currencyFormat = new Intl.NumberFormat("en-US").format(response.howMuch)
        console.log(currencyFormat)
        $("#registered-date").html(`Registered Date: ${dateToFormat.toLocaleDateString("en-GB")}`).addClass("d-flex justify-content-end");
        $("#erinnya-lyo").html(`<b>Names:</b> ${response.names}`);
        $("#no-yessimu").html(`<b>Phone Number:</b> ${response.phoneNumber}`);
        $("#wazaalibwa-ddi").html(`<b>Date of birth?:</b> ${dobToFormat.toLocaleDateString("en-GB")}`);
        $("#emyaka").html(`<b>Age:</b> ${response.age} Years Old`);
        $("#obeera-wa").html(`<b>Place Of Residence?:</b> ${response.placeOfResidence}`);
        $("#mukitundu-kino-omazeemu-banga-ki").html(`<b>Stayed there for howlong?:</b> ${response.timeOfStay}`);
        $("#wazaala-abaana").html(`<b>Do you have dependants?:</b> ${checkBoolean(response.hasDependants)}`);
        $("#bameka").html(`<b>How many are they?:</b> ${response.numberOfDependants}`);
        $("#olina-ndaga-muntu").html(`<b>Do you have a national ID?:</b> ${checkBoolean(response.hasNationalID)}`);
        $("#nin-number").html(`<b>NIN?:</b> ${response.NIN}`);
        $("#mu-biseera-byo-ebyobuvubuka-wakolanga-mulimu-ki").html(`<b>Waht was your youthhood business?:</b> ${response.youthHoodBusiness}`);
        $("#ofuna-ssente-za-gavumenti").html(`<b>Do you get Eldery Grants from Government?:</b> ${checkBoolean(response.getsGrant)}`);
        $("#ozifunidde-banga-ki").html(`<b>For how long have you been getting this/these grant(s)?:</b> ${response.forHowLong}`);
        $("#ofuna-meka").html(`<b>How much do you get?:</b> ${currencyFormat}`);
        $("#zikuyamba-zitya").html(`<b>How do these grants help you?:</b> ${response.howItHelpedYou}`);
        $("#ekibiina-kya-good-samaritan-okiganyudwamu-ki").html(`<b>How have you benefited from the Goodsamaritan Group?:</b> ${response.BenefitsFromGoodSamaritan}`);
        $("#ku-buyambi-bwa-sente-government-bweewa-ziriwa-zewali-ofunyeko").html(`<b>Which Governmenet Grant do you get?:</b> ${response.grant.GrantName} (${response.grant.GrantAbriviation})`);
        $("#webezaawo-otya").html(`<b>How do you survive?:</b> ${response.howDoYouSurvive}`);
        $("#osinzizaawa-mukama-katonda-wo").html(`<b>Where do you worship from?:</b> ${response.placeOfWorship}`);
        $("#kintu-ki-government-kyewandyagade-ekukolere-nga-omukadde").html(`<b>What would you like Government to do for you as an elderly person?:</b> ${response.yourNeedFromGovtAsAGrand}`);
        $("#magezi-ki-gowa-abavubuka-okwetegekera-obukadde").html(`<b>What advise would you give to the youth?:</b> ${response.adviseToTheYouth}`);
    })
}