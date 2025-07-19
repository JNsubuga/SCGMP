var protocol = window.location.protocol
var hostUrl = protocol + "//" + window.location.host + "/"

$(() => {
    ///////////////////////
    goodSamaritans();
    ///////////////////////////////////////////////////
    $("#search-grant-name-id").prop("disabled", true);
    /////////////////////////////////////////////////
    $('#search-gets-grant-input').change(function () {
        if (this.checked) {
            $("#search-grant-name-id").prop("disabled", false);
        } else {
            $("#search-grant-name-id").prop("disabled", true);
        }
        goodSamaritans();
    });
    /////////////////
    $("#search-grant-name-id").change(function () {
        goodSamaritans();
    });

})

const goodSamaritans = () => {
    $('#spinner-container').show();
    var auth_user_token = $('#auth-user-token').val();
    var auth_user_id = $('#auth-usser-id').val();
    let getsGrant = $("#search-gets-grant-input").is(':checked');
    let grantNameId = $("#search-grant-name-id").val()
    // console.log("HasGrant: " + getsGrant + " grantNameId: " + grantNameId);
    //////////////////////////////////////////////////////////////////
    var url = `${hostUrl}api/en/scgmp/good-samaritans/?getsGrant=${getsGrant}&grantNameId=${grantNameId}`
    $.ajax({
        "url": url,
        "method": "GET",
        "headers": {
            "Authorization": "Token " + auth_user_token
        },
        onerror: (error) => {
            $("#spinner-container").hide();
            console.log(error.responseText);
        }
    }).done((response) => {
        $('#spinner-container').hide();
        var allGoodSamaritans = [];
        for (let i = 0; i < response.length; i++) {
            var goodSamaritan = response[i];
            var dateFormat = new Date(goodSamaritan.BirthDate);
            var nameLink = `<a href="${hostUrl}good-samaritan/${goodSamaritan.id}">${goodSamaritan.names}</a>`;
            var Actions = '<button type="button" onclick="goodSamaritanForm(' + goodSamaritan.id + ')" class="btn btn-default btn-sm"><i class="fa fa-edit"></i> Edit</button>'
            allGoodSamaritans.push({
                // names: goodSamaritan.names,
                names: nameLink,
                phoneNumber: goodSamaritan.phoneNumber,
                BirthDate: dateFormat.toLocaleDateString("en-GB"),
                age: `${goodSamaritan.age} Years Old`,
                // placeOfResidence: goodSamaritan.placeOfResidence,
                // timeOfStay: goodSamaritan.timeOfStay,
                // hasDependants: goodSamaritan.hasDependants, 
                // numberOfDependants: goodSamaritan.numberOfDependants,
                // hasNationalID: goodSamaritan.hasNationalID,
                // NIN: goodSamaritan.NIN,
                // youthHoodBusiness: goodSamaritan.youthHoodBusiness,
                // getsGrant: goodSamaritan.getsGrant,
                // forHowLong: goodSamaritan.forHowLong,
                // howMuch: goodSamaritan.howMuch,
                // howItHelpedYou: goodSamaritan.howItHelpedYou,
                // BenefitsFromGoodSamaritan: goodSamaritan.BenefitsFromGoodSamaritan,
                // grant: goodSamaritan.grant.GrantName,
                // howDoYouSurvive: goodSamaritan.howDoYouSurvive,
                // placeOfWorship: goodSamaritan.placeOfWorship,
                // yourNeedFromGovtAsAGrand: goodSamaritan.yourNeedFromGovtAsAGrand,
                // adviseToTheYouth: goodSamaritan.adviseToTheYouth
                Actions
            })
        }
        const dataSet = allGoodSamaritans.map(({
            names,
            phoneNumber,
            BirthDate,
            age,
            // placeOfResidence,
            // timeOfStay,
            // hasDependants, 
            // numberOfDependants,
            // hasNationalID,
            // NIN,
            // youthHoodBusiness,
            // getsGrant,
            // forHowLong,
            // howMuch,
            // howItHelpedYou,
            // BenefitsFromGoodSamaritan,
            // grant,
            // howDoYouSurvive,
            // placeOfWorship,
            // yourNeedFromGovtAsAGrand,
            // adviseToTheYouth
            Actions
        }) => [
                names,
                phoneNumber,
                BirthDate,
                age,
                // placeOfResidence,
                // timeOfStay,
                // hasDependants, 
                // numberOfDependants,
                // hasNationalID,
                // NIN,
                // youthHoodBusiness,
                // getsGrant,
                // forHowLong,
                // howMuch,
                // howItHelpedYou,
                // BenefitsFromGoodSamaritan,
                // grant,
                // howDoYouSurvive,
                // placeOfWorship,
                // yourNeedFromGovtAsAGrand,
                // adviseToTheYouth
                Actions
            ])

        $("#goodSamaritan-data-table").DataTable({
            data: dataSet,
            responsive: true,
            lengthChange: false,
            autoWidth: false,
            bDestroy: true,
            buttons: ["copy", "csv", "excel", "pdf", "print", "colvis"],
            columns: [
                { title: "Names", width: "40%" },
                { title: "Phone Contact" },
                { title: "Date of Birth" },
                { title: "Age" },
                { title: "Action(s)", className: "dt-center" }
            ]
        })
            .buttons()
            .container()
            .appendTo('#goodSamaritan-data-table_wrapper .col-md-6:eq(0)')
    })
}

const resetForm = () => {
    $("#names").val("");
    $("#phone-number").val("");
    $("#birth-date").val("");
    $("#place-of-residence").val("");
    $("#time-of-stay").val("");
    $("#has-dependantc").val(false).prop('checked');
    $("#number-of-dependants").val("");
    $("#has-national-IDi").val(false).prop('checked');
    $("#NIN").val("");
    $("#youth-hood-business").val("");
    $("#gets-grants").val(false).prop('checked');
    $("#for-how-long").val("");
    $("#how-much").val("");
    $("#how-it-helped-you").val("");
    $("#gd-samaritan-benefits").val("");
    $("#grant-name-id").val("");
    $("#how-do-you-survive").val("");
    $("#place-of-worship").val("");
    $("#your-need-from-govt-as-a-grand").val("");
    $("#advise-to-the-youth").val("");
    $("#is-disabled").val(false).prop('checked');
}

const goodSamaritanForm = (goodSamaritanid = null) => {
    $("#modal-xl").modal('show');
    $("#form-alert").hide();
    var auth_user_token = $("#auth-user-token").val();
    var csrftoken = document.querySelector('#good-samaritan-form [name=csrfmiddlewaretoken]').value;

    if (goodSamaritanid != null) {
        $("#spinner-container-init-edit").show();
        $("#selected-good-samaritan-id").val(goodSamaritanid);
        $(".modal-title").html("Edit Record");
        $("#save-btn").html("Save Changes");
        $("#has-dependantc").html('<input class="custom-control-input" type="checkbox" id="has-dependants"><label for="has-dependants" class="custom-control-label">Has Dependants</label>');
        $("#has-national-IDi").html('<input class="custom-control-input" type="checkbox" id="has-national-ID"><label for="has-national-ID" class="custom-control-label">Has NationalID</label>');
        $("#gets-grants").html('<input class="custom-control-input" type="checkbox" id="gets-grant"><label for="gets-grant" class="custom-control-label">Gets Grant</label>');
        $("#is-disabod").html('<input class="custom-control-input" type="checkbox" id="is-disabled"><label for="is-disabled" class="custom-control-label">Disabled</label>');

        $.ajax({
            "url": hostUrl + "api/en/scgmp/good-samaritan/" + goodSamaritanid,
            "moothed": "GET",
            "headers": {
                "Authorization": "Token " + auth_user_token
            },
            onerror: (error) => {
                $("#spinner-container-init-edit").hide();
                console.log(error.responseText)
            }
        }).done((response) => {
            $("#spinner-container-init-edit").hide();
            $("#names").val(response.names);
            $("#phone-number").val(response.phoneNumber);
            $("#birth-date").val(response.BirthDate);
            $("#place-of-residence").val(response.placeOfResidence);
            $("#time-of-stay").val(response.timeOfStay);
            $("#has-dependants").val(response.hasDependants).prop('checked', response.hasDependants);
            $("#number-of-dependants").val(response.numberOfDependants);
            $("#has-national-ID").val(response.hasNationalID).prop('checked', response.hasNationalID);
            $("#NIN").val(response.NIN);
            $("#youth-hood-business").val(response.youthHoodBusiness);
            $("#gets-grant").val(response.getsGrant).prop('checked', response.getsGrant);
            $("#for-how-long").val(response.forHowLong);
            $("#how-much").val(response.howMuch);
            $("#how-it-helped-you").val(response.howItHelpedYou);
            $("#gd-samaritan-benefits").val(response.BenefitsFromGoodSamaritan),
                $("#grant-name-id").val(response.grant.id);
            $("#how-do-you-survive").val(response.howDoYouSurvive);
            $("#place-of-worship").val(response.placeOfWorship);
            $("#your-need-from-govt-as-a-grand").val(response.yourNeedFromGovtAsAGrand);
            $("#advise-to-the-youth").val(response.adviseToTheYouth);
            $("#is-disabled").val(response.is_disabled).prop('checked', response.is_disabled);
        });
    } else {
        resetForm();
        var goodSamaritanid = "null";
        $("#selected-good-samaritan-id").val(goodSamaritanid);
        $(".modal-title").html("Register Member");
        $("#save-btn").html("Submit");
        $("#has-dependantc").html('<input class="custom-control-input" type="checkbox" id="has-dependants"><label for="has-dependants" class="custom-control-label">Has Dependants</label>');
        $("#has-national-IDi").html('<input class="custom-control-input" type="checkbox" id="has-national-ID"><label for="has-national-ID" class="custom-control-label">Has NationalID</label>');
        $("#gets-grants").html('<input class="custom-control-input" type="checkbox" id="gets-grant"><label for="gets-grant" class="custom-control-label">Gets Grant</label>');
        // $("#last-row-right-col").removeClass("col-sm-6").addClass("col-sm-12");
        $("#is-disabod").html('');
    }
}

const saveData = () => {
    const csrftoken = document.querySelector('#good-samaritan-form [name=csrfmiddlewaretoken]').value;
    var auth_user_token = $("#auth-user-token").val();
    var goodSamaritanid = $("#selected-good-samaritan-id").val();
    // console.log(goodSamaritanid);
    var data = JSON.stringify({
        "names": $("#names").val(),
        "phoneNumber": $("#phone-number").val(),
        "BirthDate": $("#birth-date").val(),
        "placeOfResidence": $("#place-of-residence").val(),
        "timeOfStay": $("#time-of-stay").val(),
        "hasDependants": $("#has-dependants").is(":checked"),
        "numberOfDependants": $("#number-of-dependants").val(),
        "hasNationalID": $("#has-national-ID").is(":checked"),
        "NIN": $("#NIN").val(),
        "youthHoodBusiness": $("#youth-hood-business").val(),
        "getsGrant": $("#gets-grant").is(":checked"),
        "forHowLong": $("#for-how-long").val(),
        "howMuch": $("#how-much").val(),
        "howItHelpedYou": $("#how-it-helped-you").val(),
        "BenefitsFromGoodSamaritan": $("#gd-samaritan-benefits").val(),
        "grant": parseInt($("#grant-name-id").val()),
        "howDoYouSurvive": $("#how-do-you-survive").val(), //TextField
        "placeOfWorship": $("#place-of-worship").val(),
        "yourNeedFromGovtAsAGrand": $("#your-need-from-govt-as-a-grand").val(),  //TextField
        "adviseToTheYouth": $("#advise-to-the-youth").val(),
        "is_disabled": $("#is-disabled").is(":checked"),
    });
    // console.log(data);
    if (goodSamaritanid != 'null') {
        $.ajax({
            "url": `${hostUrl}api/en/scgmp/update/goodsamaritan/${goodSamaritanid}`,
            "method": "PUT",
            "headers": {
                "Authorization": `Token ${auth_user_token}`,
                "X-CSRFToken": csrftoken,
                "Content-Type": "application/json"
            },
            onerror: (error) => {
                $("#spinner-container").hide();
                console.log(error.responseText);
            },
            "data": data
        }).done((response) => {
            console.log(response)
            if (response.status) {
                $("#form-alert").show();
                $("#form-alert").html('<div class="alert alert-success alert-dismissible"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button><h5><i class="icon fas fa-check"></i> Success!</h5>' + response.message + '</div>');
                setTimeout(() => {
                    $("#modal-xl").modal('hide');
                }, 2000);
            } else {
                $("#form-alert").html('<div class="alert alert-danger alert-dismissible"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button><h5><i class="icon fa fa-times"></i> Error!</h5>' + response.message + '</div>');
            }
            goodSamaritans();
        });
    } else {
        // console.log(data.BirthDate)
        $.ajax({
            "url": `${hostUrl}api/en/scgmp/create/goodsamaritan/`,
            "method": "POST",
            "headers": {
                "Authorization": `Token ${auth_user_token}`,
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken
            },
            onerror: (error) => {
                $("#spinner-container").hide();
                console.log(error.responseText);
            },
            "data": data
        }).done((response) => {
            console.log(response)
            if (response.status) {
                $("#form-alert").show();
                $("#form-alert").html('<div class="alert alert-success alert-dismissible"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button><h5><i class="icon fas fa-check"></i> Success!</h5>' + response.message + '</div>');
                setTimeout(() => {
                    $("#modal-xl").modal('hide');
                }, 2000);
            } else {
                $("#form-alert").html('<div class="alert alert-danger alert-dismissible"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button><h5><i class="icon fa fa-times"></i> Error!</h5>' + response.message + '</div>');
            }
            goodSamaritans();
        })
    }
}