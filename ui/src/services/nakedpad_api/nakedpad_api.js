export class NakedPadApi {

  constructor() {
    this.API = '/api/v1';
    console.log(`Imported service nakedpad_api with API endpoint: ${this.API}`);
  }

  save(doc_id, title, text) {
    console.log('Saving...', doc_id, text);
    const doc = {
      "title": title,
      "text": text
    }
    let resp;
    console.log(doc);
    if (doc_id !== null) {
      resp = fetch(`${this.API}/documents/${doc_id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(doc)
      })
    } else { 
      resp = fetch(`${this.API}/documents`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(doc)
      });
    }
    return resp.then(response => response.json())
      .then(data => {
        doc_id = data.document.doc_id;
        console.log(data.document);
        return doc_id;
      });
  }
}

export default NakedPadApi;
