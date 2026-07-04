#ifndef LSH_ROUTER_H
#define LSH_ROUTER_H

typedef struct IngestionNode IngestionNode;
typedef struct LshCluster LshCluster;
LshCluster* init_lsh_cluster();
int calculate_lsh_bucket(float* vector);
void map_node_signature(LshCluster* lc, int id, float* vector);

#endif
