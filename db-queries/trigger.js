/**
 * this is the trigger function shall be implemented in Mongo atlas dashboard
 * for after delete operation on a user collection it will delete all events
 * without any users in database
 */
exports = async function(changeEvent) {

  // Note: In Atlas Triggers, the service name is defaulted to the cluster name.
  const serviceName = "Cluster0"; // Use your actual service/cluster name
  const dbName = "flask_agenda";

  const usersCollection = context.services.get(serviceName).db(dbName).collection("users");
  const eventsCollection = context.services.get(serviceName).db(dbName).collection("events");



  const deleteFilter = { "user_id": changeEvent.documentKey._id };
  try {
    // Fetch only the _id field from all user documents
    let arrayOfUserDocs = await usersCollection.find({},{_id:1}).toArray()
    let userIds = arrayOfUserDocs.map(doc => doc._id);

    // Build a filter to delete events whose user_id is not in the userIds array
    const deleteFilter = { "user_id": { $nin: userIds } };
    const deleteResult = await eventsCollection.deleteMany(deleteFilter);
    console.log(JSON.stringify(deleteResult));
    return deleteResult.deletedCount;

  } catch(err) {
    console.log("Failed to delete item: ", err.message);
    return { error: err.message };
  }
};


