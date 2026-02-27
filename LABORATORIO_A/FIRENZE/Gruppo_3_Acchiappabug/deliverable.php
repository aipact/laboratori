<!-- ticket_form.php -->

<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>Richiesta Assistenza CED - Comune</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; background: #eaf2fb; }
        .container { max-width: 550px; margin: 40px auto; background: #fff; padding: 2em; border-radius: 8px; box-shadow: 0 2px 8px #b0c4de; }
        h2 { color: #125488; text-align: center; }
        label { display: block; margin-top: 1.2em; font-weight: bold; }
        input[type="text"], input[type="number"], textarea {
            width: 100%; padding: 9px; border: 1px solid #b0c4de; border-radius: 4px; margin-top: .3em;
            box-sizing: border-box; resize: vertical;
        }
        input[type="file"] { margin-top: .5em;}
        button { background: #125488; color: #fff; border: none; padding: 10px 24px; margin-top: 1.2em; border-radius: 4px; cursor: pointer; }
        button:hover { background: #186cb8; }
        .success, .error { padding: 1em; margin-top: 1.5em; border-radius: 4px; text-align: center; }
        .success { background: #d3f9d8; color: #196932; }
        .error { background: #ffe0e0; color: #a82525; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Richiesta Assistenza CED</h2>
        <form id="ticketForm" name="ticketForm" enctype="multipart/form-data" method="POST">
            <label>Descrizione della richiesta*</label>
            <textarea name="descrizione" id="descrizione" rows="5" required placeholder="Dettaglia la richiesta di assistenza..."></textarea>

            <label>Tempo massimo di risposta richiesto (in ore)*</label>
            <input type="number" min="1" max="168" name="tempo_max" id="tempo_max" required placeholder="Es. 4">

            <label>Allega un file (facoltativo; max 3MB)</label>
            <input type="file" name="allegato" id="allegato" accept=".jpg,.jpeg,.png,.pdf,.doc,.docx,.xls,.xlsx,.txt">

            <button type="submit">Invia richiesta</button>
        </form>
        <div id="feedback"></div>
    </div>
<script>
document.getElementById('ticketForm').onsubmit = function(e){
    e.preventDefault();

    let descrizione = document.getElementById('descrizione').value.trim();
    let tempo = document.getElementById('tempo_max').value.trim();
    let allegato = document.getElementById('allegato').files[0];

    if(descrizione.length < 10) {
        feedback('Fornire una descrizione più dettagliata (min. 10 caratteri)', 'error');
        return false;
    }

    if(isNaN(tempo) || parseInt(tempo) < 1 || parseInt(tempo) > 168) {
        feedback('Tempo massimo di risposta non valido (da 1 a 168 ore)', 'error');
        return false;
    }

    if(allegato && allegato.size > 3*1024*1024) {
        feedback('File allegato troppo grande (max 3MB)', 'error');
        return false;
    }

    // Prepara formData per AJAX
    let formData = new FormData(document.getElementById('ticketForm'));
    let xhr = new XMLHttpRequest();
    xhr.open('POST', 'ticket_form.php', true);
    xhr.onload = function () {
        try {
            let resp = JSON.parse(xhr.responseText);
            feedback(resp.message, resp.status);
            if(resp.status === 'success') {
                document.getElementById('ticketForm').reset();
            }
        } catch(e){
            feedback('Errore imprevisto nella risposta dal server.', 'error');
        }
    };
    xhr.send(formData);
    return false;
};

function feedback(msg, type) {
    document.getElementById('feedback').innerHTML = `<div class="${type}">${msg}</div>`;
}
</script>
<?php
// SECTION BACKEND: Salva la richiesta su file CSV e allegato
if($_SERVER['REQUEST_METHOD'] === 'POST') {
    $desc = trim($_POST['descrizione'] ?? '');
    $tempo = intval($_POST['tempo_max'] ?? 0);

    if(strlen($desc) < 10 || $tempo < 1 || $tempo > 168) {
        echo json_encode(['status'=>'error','message'=>'Dati non validi.']);
        exit;
    }

    // Gestione allegato
    $allegato_nome = "";
    $upload_dir = __DIR__ . "/uploads/";
    if(!is_dir($upload_dir)) mkdir($upload_dir, 0775, true);

    if(isset($_FILES['allegato']) && $_FILES['allegato']['tmp_name']) {
        $size = $_FILES['allegato']['size'];
        if($size > 3*1024*1024) {
            echo json_encode(['status'=>'error','message'=>'Il file è troppo grande.']);
            exit;
        }
        $safe_name = date('Ymd_His').'_'.basename($_FILES['allegato']['name']);
        $allegato_nome = preg_replace('/[^\w\.\-]/', '_', $safe_name);
        if(!move_uploaded_file($_FILES['allegato']['tmp_name'], $upload_dir . $allegato_nome)) {
            echo json_encode(['status'=>'error','message'=>'Errore nel salvataggio dell\'allegato.']);
            exit;
        }
    }

    // Salva richiesta in CSV (in append)
    $csv = __DIR__ . '/richieste_ced.csv';
    $riga = '"'.date('Y-m-d H:i:s').'";"'.str_replace('"','""',$desc).'";'.$tempo.';"'.$allegato_nome.'"'."\n";
    file_put_contents($csv, $riga, FILE_APPEND);

    echo json_encode(['status'=>'success','message'=>'Richiesta inviata con successo! Riceverai riscontro al più presto.']);
    exit;
}
?>
</body>
</html>
