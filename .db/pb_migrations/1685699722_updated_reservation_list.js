migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("v8cua5zxvjxe0mo")

  // remove
  collection.schema.removeField("gl2nczef")

  // remove
  collection.schema.removeField("g2mekoqu")

  // remove
  collection.schema.removeField("bfavk6uh")

  // remove
  collection.schema.removeField("ui2moic5")

  // remove
  collection.schema.removeField("4ol4f7hf")

  // remove
  collection.schema.removeField("yjgoqm6h")

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("v8cua5zxvjxe0mo")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "gl2nczef",
    "name": "reservation_date",
    "type": "relation",
    "required": false,
    "unique": false,
    "options": {
      "collectionId": "1rm9eqlfw2z6co2",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": 1,
      "displayFields": [
        "reservation_date"
      ]
    }
  }))

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "g2mekoqu",
    "name": "customer_id",
    "type": "relation",
    "required": false,
    "unique": false,
    "options": {
      "collectionId": "1rm9eqlfw2z6co2",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": 1,
      "displayFields": [
        "id"
      ]
    }
  }))

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "bfavk6uh",
    "name": "customer_name",
    "type": "relation",
    "required": false,
    "unique": false,
    "options": {
      "collectionId": "1rm9eqlfw2z6co2",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": 1,
      "displayFields": [
        "last_name",
        "first_name"
      ]
    }
  }))

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "ui2moic5",
    "name": "room_number",
    "type": "relation",
    "required": false,
    "unique": false,
    "options": {
      "collectionId": "x0hmwdlv02zwb5y",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": 1,
      "displayFields": [
        "room_number"
      ]
    }
  }))

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "4ol4f7hf",
    "name": "room_type",
    "type": "relation",
    "required": false,
    "unique": false,
    "options": {
      "collectionId": "kigjd431nqoyf61",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": 1,
      "displayFields": [
        "type",
        "price"
      ]
    }
  }))

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "yjgoqm6h",
    "name": "duration",
    "type": "relation",
    "required": false,
    "unique": false,
    "options": {
      "collectionId": "1rm9eqlfw2z6co2",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": 1,
      "displayFields": [
        "check_in",
        "check_out"
      ]
    }
  }))

  return dao.saveCollection(collection)
})
