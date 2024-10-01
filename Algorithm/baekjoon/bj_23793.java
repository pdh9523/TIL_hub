Class Main {

	static class Node implements Comparable<Node> {
		int x;
		int weight;

		public Node(int x, int weight) {
			this.x = x;
			this.weight = weight;
		}
		
		@Override
		public int compareTo(Node o) {
			return this.weight - o.weight;
		}
	}

	private static ArrayList<ArrayList<Node>> graph;
	private static int[] distance;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		graph = new ArrayList<>();
		for (int i=0; i<=N; i++) {
			graph.add(new ArrayList<>());
		}

		for (int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());

			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int weight = Integer.parseInt(st.nextToken());

			graph.get(a).add(new Node(b,weight));
		}
		st = new StringTokenizer(br.readLine());
		int start = Integer.parseInt(br.readLine());
		int mid = Integer.parseInt(br.readLine());
		int end = Integer.parseInt(br.readLine());

		int res1 = dijkstra(start,mid) + dijkstra(mid, end)
		int res2 = dijkstra(start,end)
		System.out.println(res1+" "+res2)
	}

	private int dijkstra(int s, int e) {
		distance = new int[N+1];
		Arrays.fill(distnace, Integer.MAX_VALUE);
		distance[s] = 0;
		PriorityQueue<Node> pq = new PriorityQueue<>(); 
		pq.add(new Node(s,0));
		while (!pq.isEmpty()) {
			Node node = pq.poll();

			if (node.weight > distance[node.x]) continue;

			ArrayList<Node> nextNodes = graph.get(node.x)
			for (Node next: nextNodes) {
				int cost = next.weight + node.weight
				if (distnace[next.x] > cost) {
					distnace[next.x] = cost;
					pq.add(new Node(next.x, cost));
				}
			}
		}

		return distnace[e];
	}
}