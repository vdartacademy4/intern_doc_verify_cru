// =======================================
// AI Intern Verification Registry
// =======================================

let candidates = [];
let filteredCandidates = [];

let activeFilter = "ALL";


// =======================================
// Dashboard Statistics
// =======================================

async function loadStats() {

    try {

        const response = await fetch("/stats");

        const stats = await response.json();

        document.getElementById("total").innerText =
            stats.total || 0;

        document.getElementById("verified").innerText =
            stats.verified || 0;

        document.getElementById("manual").innerText =
            stats.manual || 0;

        document.getElementById("mismatch").innerText =
            stats.mismatch || 0;

    }

    catch (err) {

        console.log(err);

    }

}



// =======================================
// Load Candidates
// =======================================

async function loadCandidates() {

    try {

        const response = await fetch("/candidates");

        candidates = await response.json();

        // Latest processed email first
        candidates.sort((a, b) => {

            const da = new Date(
                (a.Processed_Date || "") + " " +
                (a.Processed_Time || "")
            );

            const db = new Date(
                (b.Processed_Date || "") + " " +
                (b.Processed_Time || "")
            );

            return db - da;

        });

        filteredCandidates = [...candidates];

        renderTable();

    }

    catch (err) {

        console.log(err);

    }

}



// =======================================
// Status Badge
// =======================================

function getStatusClass(status) {

    status = (status || "").toUpperCase();

    if (status.includes("VERIFIED"))
        return "status status-verified";

    if (status.includes("MANUAL"))
        return "status status-manual";

    if (status.includes("MISMATCH"))
        return "status status-mismatch";

    return "status status-missing";

}



// =======================================
// Search
// =======================================

function searchCandidates(value) {

    value = value.toLowerCase();

    filteredCandidates = candidates.filter(c => {

        return (

            (c.Candidate_Name || "")
                .toLowerCase()
                .includes(value)

            ||

            (c.Email || "")
                .toLowerCase()
                .includes(value)

            ||

            (c.College || "")
                .toLowerCase()
                .includes(value)

            ||

            (c.Folder_Name || "")
                .toLowerCase()
                .includes(value)

            ||

            (c.Intern_Domain || "")
                .toLowerCase()
                .includes(value)

            ||

            (c.Enrollment_ID || "")
                .toLowerCase()
                .includes(value)

        );

    });

    applyFilter();

}



// =======================================
// Date Filter
// =======================================

function filterByDate() {

    const selected =
        document.getElementById("dateFilter").value;

    if (selected === "") {

        filteredCandidates = [...candidates];

        applyFilter();

        return;

    }

    filteredCandidates = candidates.filter(c => {

        return c.Processed_Date === selected;

    });

    applyFilter();

}



// =======================================
// Status Filter
// =======================================

function setFilter(filter) {

    activeFilter = filter;

    document.querySelectorAll(".filter").forEach(btn => {

        btn.classList.remove("active");

        if (btn.dataset.filter === filter) {

            btn.classList.add("active");

        }

    });

    applyFilter();

}



function applyFilter() {

    if (activeFilter === "ALL") {

        renderTable();

        return;

    }

    const temp = filteredCandidates.filter(c => {

        return (c.Final_Status || "")
            .toUpperCase()
            .includes(activeFilter);

    });

    const backup = filteredCandidates;

    filteredCandidates = temp;

    renderTable();

    filteredCandidates = backup;

}
// =======================================
// Render Candidate Table
// =======================================

function renderTable() {

    const table = document.getElementById("candidateTable");

    table.innerHTML = "";

    if (filteredCandidates.length === 0) {

        table.innerHTML = `
        <tr>
            <td colspan="5" style="padding:30px;text-align:center;">
                No Candidates Found
            </td>
        </tr>
        `;

        return;

    }

    filteredCandidates.forEach(candidate => {

        const status = candidate.Final_Status || "";

        table.innerHTML += `

        <tr onclick="openDrawer('${candidate.Folder_Name}')">

            <td>
                <strong>${candidate.Candidate_Name || "Name Pending"}</strong>
                <br>
                <small>${candidate.Folder_Name}</small>
            </td>

            <td>
                <span class="${getStatusClass(status)}">
                    ${status}
                </span>
            </td>

            <td>
                ${candidate.Processed_Date || "-"}
            </td>

            <td>
                ${candidate.Email || "-"}
            </td>

             <td>${candidate.Technology || "-"}</td>

            <td>
                ${candidate.Enrollment_ID || "-"}
            </td>

        </tr>

        `;

    });

}



// =======================================
// Open Candidate Drawer
// =======================================

function openDrawer(folderName) {

    const candidate =
        candidates.find(c => c.Folder_Name === folderName);

    if (!candidate) return;

    document.getElementById("overlay").style.display = "block";

    document.getElementById("detailsPanel")
        .classList.add("show");



    // Header

    document.getElementById("candidateName").innerText =
        candidate.Candidate_Name || "Candidate";

    document.getElementById("candidateStatus").innerHTML =

        `<span class="${getStatusClass(candidate.Final_Status)}">

            ${candidate.Final_Status || "UNKNOWN"}

        </span>`;


    // Basic Information

    document.getElementById("detailName").innerText =
        candidate.Candidate_Name || "-";

    document.getElementById("detailEmail").innerText =
        candidate.Email || "-";

    document.getElementById("detailPhone").innerText =
        candidate.Phone || "-";

    document.getElementById("detailCollege").innerText =
        candidate.College || "-";

    document.getElementById("detailDomain").innerText =
        candidate.Technology || "-";

    document.getElementById("detailEnrollment").innerText =
        candidate.Enrollment_ID || "-";

    document.getElementById("detailRegister").innerText =
        candidate.Register_Number || "-";

    document.getElementById("detailAadhaar").innerText =
        candidate.Aadhaar_Number || "-";

    document.getElementById("detailStart").innerText =
        candidate.Start_Date || "-";

    document.getElementById("detailEnd").innerText =
        candidate.End_Date || "-";



    // Verification Status

    document.getElementById("resumeStatus").innerHTML =

        `<span class="${getStatusClass(candidate.Resume_Name_Status)}">

            ${candidate.Resume_Name_Status || "-"}

        </span>`;


    document.getElementById("aadhaarStatus").innerHTML =

        `<span class="${getStatusClass(candidate.Aadhaar_Status)}">

            ${candidate.Aadhaar_Status || "-"}

        </span>`;


    document.getElementById("collegeStatus").innerHTML =

        `<span class="${getStatusClass(candidate.CollegeID_Status)}">

            ${candidate.CollegeID_Status || "-"}

        </span>`;


    document.getElementById("offerStatus").innerHTML =

        `<span class="${getStatusClass(candidate.OfferLetter_Status)}">

            ${candidate.OfferLetter_Status || "-"}

        </span>`;


    // Missing Documents

    document.getElementById("missingDocs").innerText =
        candidate.Missing_Documents || "None";



    // Uploaded Files

    const uploadedFiles =
        document.getElementById("uploadedFiles");

    uploadedFiles.innerHTML = "";

    if (candidate.Uploaded_Files &&
        candidate.Uploaded_Files.trim() !== "") {

        const files =
            candidate.Uploaded_Files.split(",");

        files.forEach(file => {

            const filename = file.trim();

            uploadedFiles.innerHTML += `

            <div style="
                margin-bottom:10px;
                padding:10px;
                border:1px solid #ddd;
                border-radius:8px;
                background:#fafafa;
            ">

                📄

                <a href="/file/${candidate.Folder_Name}/${encodeURIComponent(filename)}"

                   target="_blank">

                    ${filename}

                </a>

            </div>

            `;

        });

    }

    else {

        uploadedFiles.innerHTML =

            "<p>No Uploaded Files</p>";

    }

}
// =======================================
// Close Drawer
// =======================================

function closeDrawer() {

    document.getElementById("detailsPanel")
        .classList.remove("show");

    document.getElementById("overlay")
        .style.display = "none";

}



// =======================================
// Process Gmail
// =======================================

async function processEmails() {

    document.getElementById("loading")
        .style.display = "flex";

    document.getElementById("processBtn")
        .disabled = true;

    try {

        const response = await fetch("/process");

        const result = await response.json();

        alert(result.message);

        // Reload latest data
        await loadStats();

        await loadCandidates();

    }

    catch (err) {

        console.log(err);

        alert("Server Error");

    }

    document.getElementById("loading")
        .style.display = "none";

    document.getElementById("processBtn")
        .disabled = false;

}



// =======================================
// Window Load
// =======================================

window.onload = async function () {

    await loadStats();

    await loadCandidates();

};



// =======================================
// Auto Refresh Every 10 Seconds
// =======================================

setInterval(async () => {

    await loadStats();

    await loadCandidates();

}, 10000);



// =======================================
// Search Box
// =======================================

document.getElementById("search")
.addEventListener("keyup", function (e) {

    searchCandidates(e.target.value);

});



// =======================================
// Date Filter
// =======================================

const dateFilter =
    document.getElementById("dateFilter");

if (dateFilter) {

    dateFilter.addEventListener("change", filterByDate);

}



// =======================================
// Status Buttons
// =======================================

document.querySelectorAll(".filter").forEach(btn => {

    btn.addEventListener("click", function () {

        setFilter(btn.dataset.filter);

    });

});



// =======================================
// Process Button
// =======================================

document.getElementById("processBtn")
.addEventListener("click", processEmails);



// =======================================
// Close Drawer Button
// =======================================

document.getElementById("closeDrawer")
.addEventListener("click", closeDrawer);



// =======================================
// Overlay Click
// =======================================

document.getElementById("overlay")
.addEventListener("click", closeDrawer);



// =======================================
// ESC Key Close Drawer
// =======================================

document.addEventListener("keydown", function (e) {

    if (e.key === "Escape") {

        closeDrawer();

    }

});



// =======================================
// End of Script
// =======================================