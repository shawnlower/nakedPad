export class Ltp {
  constructor() {
    console.log('Imported service Ltp');
  }

  getItems() {
    return new Promise((resolve, reject) => {
    const response = {
      "data": [
        {
          "item_id": "ontology-mapping-the-state-of-the-art",
          "item_type": "Book",
          "name": "Ontology Mapping: The State of the Art"
        },
        {
          "item_id": "ontology-mapping-the-state-of-the-art0",
          "item_type": "Book",
          "name": "Ontology Mapping: The State of the Art"
        },
        {
          "item_id": "lord-of-the-rings",
          "item_type": "Book",
          "name": "Lord of the Rings"
        },
        {
          "item_id": "war-of-the-worlds",
          "item_type": "Book",
          "name": "War of the Worlds"
        },
        {
          "item_id": "car-pc-hacks",
          "item_type": "Book",
          "name": "Car PC Hacks"
        },
        {
          "item_id": "shawn-lower",
          "item_type": "Person",
          "name": "Shawn Lower"
        },
        {
          "item_id": "robert-downey-jr",
          "item_type": "Person",
          "name": "Robert Downey Jr."
        }
      ],
      "more": false,
      "results": 7
    }
    resolve(response);
  });
  }
}

export default Ltp;
