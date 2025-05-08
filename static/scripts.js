document.addEventListener("DOMContentLoaded", function () {
    const checkbox = document.getElementById('toggle-switch');
    const uploadBlock = document.getElementById('uploadBlock');
    const fileInput = document.getElementById('fileInput');
  
    function toggleUploadBlock() {
      if (checkbox.checked) {
        uploadBlock.classList.add('d-none');
        fileInput.removeAttribute('required');
      } else {
        uploadBlock.classList.remove('d-none');
        fileInput.setAttribute('required', 'required');
      }
    }
  
    checkbox.addEventListener('change', toggleUploadBlock);
  
    toggleUploadBlock();
});
  
document.addEventListener('DOMContentLoaded', function () {
    const toggleSwitch = document.getElementById("toggle-switch");
    const metricsCheckbox = document.getElementById("calculate_metrics");

    toggleSwitch.addEventListener("change", toggleGroundTruthField);
    metricsCheckbox.addEventListener("change", toggleGroundTruthField);

    toggleGroundTruthField();
});


document.addEventListener('DOMContentLoaded', function() 
{
    document.getElementById("noise_check").addEventListener("change", toggleNoiseFields);

    document.getElementById("noise_type").addEventListener("change", function() 
    {
        document.getElementById("noise_value").value = 0;
        toggleNoiseFields();
    });
});

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

function toggleNoiseFields() 
{
    var checkbox = document.getElementById("noise_check");
    var noiseFields = document.getElementById("noise_fields");
    var noiseType = document.getElementById("noise_type").value;
    var noiseParameterInput = document.getElementById("noise_value");

    if (checkbox.checked) 
    {
        noiseFields.style.display = "block";
        noiseParameterInput.setAttribute("min", "0");
        noiseParameterInput.setAttribute("max", "0.1");
        noiseParameterInput.setAttribute("step", "0.005");
    } 
    else 
    {
        noiseFields.style.display = "none";
    }
}

function toggleGroundTruthField() {
    const metricsCheck = document.getElementById("calculate_metrics");
    const metricsFields = document.getElementById('metrics_fields');
    const groundTruthInput = document.getElementsByName("ground_truth")[0];
    const infoMessage = document.getElementById('bsds-message');
    const useBsds = document.getElementById("toggle-switch").checked;

    if (metricsCheck.checked && !useBsds) 
    {
        metricsFields.style.display = 'block';
        groundTruthInput.required = true;
        infoMessage.hidden = true;
    } 
    else if (metricsCheck.checked && useBsds) 
    {
        metricsFields.style.display = 'none';
        groundTruthInput.required = false;
        infoMessage.hidden = false;
    } 
    else 
    {
        metricsFields.style.display = 'none';
        groundTruthInput.required = false;
        infoMessage.hidden = true;
    }
}

function validateForm() {
    const useBsds = document.getElementById("toggle-switch").checked;
    const metricsCheck = document.getElementById("calculate_metrics").checked;

    const mainFilesInput = document.getElementsByName("file")[0];
    const mainFiles = mainFilesInput.files;

    const gtFilesInput = document.getElementsByName("ground_truth")[0];
    const gtFiles = gtFilesInput.files;

    if (!useBsds) {
        if (mainFiles.length === 0) {
            alert("Please upload at least one image.");
            return false;
        }

        if (mainFiles.length > 10) {
            alert("You can upload at most 10 images.");
            return false;
        }

        for (let i = 0; i < mainFiles.length; i++) {
            if (
                mainFiles[i].size > 1 * 1024 * 1024 ||
                (gtFiles[i] && gtFiles[i].size > 1 * 1024 * 1024)
            ) {
                alert("Image size should be less than 1 MB.");
                return false;
            }
        }

        if (metricsCheck) {
            if (mainFiles.length !== gtFiles.length) {
                alert("Number of original images must match number of ground truth images.");
                return false;
            }
        }
    }

    return true;
}