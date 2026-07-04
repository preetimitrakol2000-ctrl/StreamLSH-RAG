#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define BUCKETS 4
#define DIM 4

typedef struct {
    int collection_id;
    float signatures[DIM];
} IngestionNode;

typedef struct {
    IngestionNode registers[8];
    int count;
} LshCluster;

#ifdef _WIN32
    __declspec(dllexport) LshCluster* init_lsh_cluster();
    __declspec(dllexport) void map_node_signature(LshCluster* lc, int id, float* vector);
    __declspec(dllexport) int calculate_lsh_bucket(float* vector);
#endif

LshCluster* init_lsh_cluster() {
    LshCluster* lc = (LshCluster*)malloc(sizeof(LshCluster));
    lc->count = 0;
    return lc;
}

int calculate_lsh_bucket(float* vector) {
    // Basic projection logic: check sign profiles to yield integer hash mappings
    int hash_code = 0;
    if (vector[0] >= 0.0f) hash_code |= 1;
    if (vector[1] >= 0.0f) hash_code |= 2;
    return hash_code % BUCKETS;
}

void map_node_signature(LshCluster* lc, int id, float* vector) {
    int idx = lc->count;
    lc->registers[idx].collection_id = id;
    for (int i = 0; i < DIM; i++) lc->registers[idx].signatures[i] = vector[i];
    lc->count++;
}
