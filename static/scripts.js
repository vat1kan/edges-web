function toggleNoiseFields() 
{
    var checkbox = document.getElementById("noise_check");
    var noiseFields = document.getElementById("noise_fields");
    var noiseType = document.getElementById("noise_type").value;
    var noiseParameterInput = document.getElementById("noise_parameter");

    if (checkbox.checked) 
    {
        noiseFields.style.display = "block";
        if (noiseType == "gauss") {
            noiseParameterInput.setAttribute("min", "0");
            noiseParameterInput.setAttribute("max", "100");
            noiseParameterInput.setAttribute("step", "5");
        } 
        else 
        {
            noiseParameterInput.setAttribute("min", "0");
            noiseParameterInput.setAttribute("max", "1");
            noiseParameterInput.setAttribute("step", "0.05");
        }
    } 
    else 
    {
        noiseFields.style.display = "none";
    }
}

document.addEventListener('DOMContentLoaded', function() 
{
    document.getElementById("noise_check").addEventListener("change", toggleNoiseFields);

    document.getElementById("noise_type").addEventListener("change", function() 
    {
        document.getElementById("noise_parameter").value = 0;
        toggleNoiseFields();
    });
});


function toggleGroundTruthField() 
{
    var metricsCheck = document.getElementById("calculate_metrics");
    var metricsFields = document.getElementById('metrics_fields');
    var groundTruthInput = document.getElementsByName("ground_truth")[0];

    if (metricsCheck.checked) 
    {
        metricsFields.style.display = 'block';
        groundTruthInput.required = true;
    } 
    else 
    {
        metricsFields.style.display = 'none';
        groundTruthInput.required = false;
    }
}

function validateForm() 
{
    var metricsCheck = document.getElementById("calculate_metrics");
    var mainFilesInput = document.getElementsByName("file")[0];
    var mainFiles = mainFilesInput.files;
    var gtFilesInput = document.getElementsByName("ground_truth")[0];
    var gtFiles = gtFilesInput.files;

    if (mainFiles.length === 0) 
    {
        alert("Please upload at least one image.");
        return false;
    }

    if (mainFiles.length > 30) 
    {
        alert("You can upload at most 30 images.");
        return false;
    }

    for (var i = 0; i < mainFiles.length; i++) 
    {
        if (mainFiles[i].size > 5 * 1024 * 1024 || gtFiles[i].size > 5 * 1024 * 1024) 
        {
            alert("Image size should be less than 5 MB.");
            return false;
        }
    }

    if (metricsCheck.checked) 
    {
        var groundTruthFiles = document.getElementsByName("ground_truth")[0].files;

        if (mainFiles.length !== groundTruthFiles.length) {
            alert("Number of original images must match number of ground truth images.");
            return false;
        }

        return true;
    }
}


document.addEventListener('DOMContentLoaded', function() 
{
    var accordion = document.getElementById("detailsButton");
    accordion.addEventListener("click", function() 
    {
        this.classList.toggle("active");
        var panel = document.getElementById("errorDetails");
        if (panel.style.display === "block") 
        {
            panel.style.display = "none";
        } 
        else 
        {
            panel.style.display = "block";
        }
    });
});

