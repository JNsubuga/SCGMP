var protocol = window.location.protocol
var hostUrl = protocol + "//" + window.location.host + "/"


$(() => {
    grants();
})

const grants = () => {
    $('#spinner-container').show();
    var auth_user_token = $('#auth-user-token').val();
    // var auth_user_id = $('#auth-user-id').val();

    $.ajax({
        "url": hostUrl + "api/en/scgmp/grants/",
        "method": "GET",
        "headers": {
            "Authorization": "Token " + auth_user_token
        },
        onerror: (error) => {
            $("#spinner-container").hide();
            console.log(error.responseText);
        }
    }).done((response)=>{
        // console.log(response)
        $('#spinner-container').hide();
        var allGrants = [];
        for(let i = 0; i < response.length; i++) {
            var grant = response[i];
            var dateFormat = new Date(grant.created)
            var Actions = '<button type="button" onclick="grantForm(' + grant.id + ')" class="btn btn-default btn-sm"><i class="fa fa-edit"></i> Edit</button>';
            allGrants.push({
                GrantName: grant.GrantName,
                GrantAbriviation: grant.GrantAbriviation,
                // created: dateFormat.toLocaleDateString("en-GB"),
                Actions
            })
        }

        const dataSet = allGrants.map(({GrantName, GrantAbriviation, /*created,*/ Actions}) => [GrantName, GrantAbriviation, /*created,*/ Actions]);

        $("#grant-data-table").DataTable({
            data: dataSet,
            responsive: true,
            lengthChange: false,
            autoWidth: false,
            bDestroy: true,
            buttons: ["copy", "csv", "excel", "pdf", "print", "colvis"],
            columns: [
                {title: "Grant Name"},
                {title: "Grant Abbriviation"},
                // {title: "Date"},
                {title: "Action", className: "dt-center"}
            ]
        })
        .buttons()
        .containers()
        .appendTo('#grant-data-table_wrapper .col-md-6:eq(0)')
    })
}

const resetForm = () => {
    $("#grant-name").val("");
    $("#grant-abriviation").val("");
}

const grantForm = (grantid = null) => {
    $("#modal-xl").modal('show');
    $("#form-alert").hide();
    var auth_user_token = $("#auth-user-token").val();
    const csrftoken = document.querySelector('#grant-form [name=csrfmiddlewaretoken]').value;
    if(grantid != null){
        $("#spinner-container-init-edit").show();
        $("#selected-grant-id").val(grantid);
        $(".modal-title").html("Edit Record");
        $("#save-btn").html("Save Changes");
        $("#is-disabod").html('<input class="custom-control-input" type="checkbox" id="is-disabled" /><label for="is-disabled" class="custom-control-label">Disabled</label>');

        $.ajax({
            "url": hostUrl + "api/en/scgmp/grant/" + grantid,
            "method": "GET",
            "headers": {
                "Authorization": "Token " + auth_user_token
            },
            onerror: (error) => {
                $("#spinner-container-init-edit").hide();
                console.log(error.responseText);
            }
        }).done((response) => {
            // console.log(response)
            $("#spinner-container-init-edit").hide();
            $("#grant-name").val(response.GrantName);
            $("#grant-abriviation").val(response.GrantAbriviation);
            $("#is-disabled").val(response.is_disabled).prop('checked', response.is_disabled);
        });
    } else {
        resetForm();
        var grantid = "null";
        $("#selected-grant-id").val(grantid);
        $(".model-title").html("Register Grant");
        $("#save-btn").html("Submit");
        $("#is-disabod").html('');
    }
}

const saveData = () => {
    const csrftoken = document.querySelector('#grant-form [name=csrfmiddlewaretoken]').value;
    var auth_user_token = $("#auth-user-token").val();
    var grantid = $("#selected-grant-id").val();
    $("#spinner-container").show();

    var data = JSON.stringify({
        "GrantName": $("#grant-name").val(),
        "GrantAbriviation": $("#grant-abriviation").val(),
        "is_disabled": $("#is-disabled").is(":checked")
    })

    if(grantid != "null"){
        $.ajax({
            "url": hostUrl + "api/en/scgmp/update/grant/" + grantid,
            "method": "PUT",
            "headers": {
                "Authorization": "Token " + auth_user_token,
                "X-CSRFToken": csrftoken,
                "Content-Type": "application/json"
            }, 
            onerror: (error) => {
                $("#spinner-container").hide();
                console.log(error, responseText);
            }, 
            "data": data
        }).done((response) => {
            if(response.status){
                $("#form-alert").show();
                $("#form-alert").html('<div class="alert alert-success alert-dismissible"><button type="button" class="close"data-dismiss="alert" aria-hidden="true">&times;</button><h5><i class="icon fas fa-check"></i> Success!</h5>' + response.message + '</div>');
                setTimeout(() => {
                    $("#modal-xl").modal('hide');
                }, 2000);
            } else {
                $("#form-alert").html('<div class="alert alert-danger alert-dismissible"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button><h5><i class="icon fa fa-times"></i> Error!</h5>' + response.message + '</div>');
            }
            grants();
        });
    } else {
        $.ajax({
            "url": hostUrl + "api/en/scgmp/register/grant",
            "method": "POST",
            "headers": {
                "Authorization": "Token " + auth_user_token,
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken
            },
            "data": data
        }).done((response)=>{
            // console.log(response);
            if (response.status) {
                $('#form-alert').show();
                $("#form-alert").html('<div class="alert alert-success alert-dismissible"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button><h5><i class="icon fas fa-check"></i> Success!</h5>' + response.message + '</div>');
                setTimeout(() => {
                  $("#modal-xl").modal('hide');
                }, 2000);
              } else {
                $("#form-alert").html('<div class="alert alert-danger alert-dismissible"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button><h5><i class="icon fa fa-times"></i> Error!</h5>' + response.message + '</div>');
            }
            // console.log(response);
            grants();
        })
    }
}