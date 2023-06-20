migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("v8cua5zxvjxe0mo")

  // remove
  collection.schema.removeField("fpaqdezr")

  // remove
  collection.schema.removeField("bpeftatu")

  // remove
  collection.schema.removeField("buy9lsz8")

  // remove
  collection.schema.removeField("wubi4oym")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "t4cjilpb",
    "name": "customer",
    "type": "relation",
    "required": false,
    "unique": false,
    "options": {
      "collectionId": "ouc9mg423fntace",
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
    "id": "pmcljjdc",
    "name": "email",
    "type": "relation",
    "required": false,
    "unique": false,
    "options": {
      "collectionId": "ouc9mg423fntace",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": 1,
      "displayFields": [
        "email"
      ]
    }
  }))

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "x80iee0f",
    "name": "contact_number",
    "type": "relation",
    "required": false,
    "unique": false,
    "options": {
      "collectionId": "ouc9mg423fntace",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": 1,
      "displayFields": [
        "contact"
      ]
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("v8cua5zxvjxe0mo")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "fpaqdezr",
    "name": "last_name",
    "type": "text",
    "required": false,
    "unique": false,
    "options": {
      "min": null,
      "max": null,
      "pattern": ""
    }
  }))

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "bpeftatu",
    "name": "first_name",
    "type": "text",
    "required": false,
    "unique": false,
    "options": {
      "min": null,
      "max": null,
      "pattern": ""
    }
  }))

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "buy9lsz8",
    "name": "contact_number",
    "type": "number",
    "required": false,
    "unique": false,
    "options": {
      "min": null,
      "max": null
    }
  }))

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "wubi4oym",
    "name": "email",
    "type": "email",
    "required": false,
    "unique": false,
    "options": {
      "exceptDomains": null,
      "onlyDomains": null
    }
  }))

  // remove
  collection.schema.removeField("t4cjilpb")

  // remove
  collection.schema.removeField("pmcljjdc")

  // remove
  collection.schema.removeField("x80iee0f")

  return dao.saveCollection(collection)
})
