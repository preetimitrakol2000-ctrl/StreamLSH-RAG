from lsh_bridge import LshBridge

if __name__ == "__main__":
    router = LshBridge()

    # Route real-time continuous threat alert vectors to localized approximation buckets
    router.process_node_data(801, [0.55, 0.12, -0.45, 0.22])
    
    alert_vector = [0.61, 0.05, -0.32, 0.14]
    assigned_bucket = router.route_vector_query(alert_vector)

    print("=== STREAMLSH-RAG APPROXIMATION ROUTER ===")
    print(f"[*] Query matched LSH Hyperplane Segment Bucket Index Target: Bin [{assigned_bucket}]")
