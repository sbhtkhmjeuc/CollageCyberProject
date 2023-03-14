#include <bson/bson.h>
#include <mongoc/mongoc.h>
#include <stdio.h>

int main()
{
    mongoc_client_t *client;
    mongoc_database_t *database;
    mongoc_collection_t *cmd_collection, *dns_collection;
    bson_error_t error;
    bson_t *cmd_doc, *dns_doc;
    char *uri_string = "mongodb+srv://sbhtkhmjeuc:***@cluster0.a52tjwe.mongodb.net/?retryWrites=true&w=majority";
    const char *cmd_db_name = "CollageCyberProject";
    const char *cmd_coll_name = "CMDCommmands";
    const char *dns_coll_name = "DNSRequests";
    mongoc_init();

    client = mongoc_client_new(uri_string);
    if (!client)
    {
        fprintf(stderr, "Failed to parse URI\n");
        return EXIT_FAILURE;
    }

    database = mongoc_client_get_database(client, cmd_db_name);
    cmd_collection = mongoc_client_get_collection(client, cmd_db_name, cmd_coll_name);
    dns_collection = mongoc_client_get_collection(client, cmd_db_name, dns_coll_name);

    cmd_doc = bson_new();
    bson_append_utf8(cmd_doc, "command", -1, "whoami", -1);
    if (!mongoc_collection_insert_one(cmd_collection, cmd_doc, NULL, NULL, &error))
    {
        fprintf(stderr, "%s\n", error.message);
    }
    bson_destroy(cmd_doc);

    dns_doc = bson_new();
    bson_append_utf8(dns_doc, "request", -1, "https://google.com", -1);
    if (!mongoc_collection_insert_one(dns_collection, dns_doc, NULL, NULL, &error))
    {
        fprintf(stderr, "%s\n", error.message);
    }
    bson_destroy(dns_doc);

    mongoc_collection_destroy(cmd_collection);
    mongoc_collection_destroy(dns_collection);
    mongoc_database_destroy(database);
    mongoc_client_destroy(client);
    mongoc_cleanup();

    return 0;
}
