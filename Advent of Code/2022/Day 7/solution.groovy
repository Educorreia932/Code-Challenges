class Node {
    public String name
    public Node parent
    public HashMap<String, Node> children = [:]
    public boolean isFile
    public Integer size

    Node(String name, Node parent = null, isFile = false, size = 0) {
        this.name = name
        this.parent = parent
        this.isFile = isFile
        this.size = size
    }

    Node addDirectory(String name) {
        children[name] = new Node(name, this)
    }

    void addFile(String name, Integer size) {
        children[name] = new Node(name, this, true, size)

        Node parent = this

        while (parent != null) {
            parent.size += size
            parent = parent.parent
        }
    }

    List<Node> toList() {
        return [this] + (children.collect { _, node -> node.toList() } as Collection<Node>)
    }
}

static readInput() {
    def rootNode = new Node("")
    Node currentNode = rootNode

    new File("input.txt").eachLine { line ->
        if (line.charAt(0) == ('$' as char)) {
            if (line.substring(2, 4) == "cd") {
                def directoryName = line.substring(5)

                if (directoryName == "..")
                    currentNode = currentNode.parent

                else
                    currentNode = currentNode.addDirectory(directoryName)
            }
        }

        else {
            def tokens = line.split()

            if (tokens[0] != "dir") {
                def fileSize = tokens[0] as Integer
                def fileName = tokens[1]

                currentNode.addFile(fileName, fileSize)
            }
        }
    }

    return rootNode
}

static Integer partOne(Node rootNode) {
    return rootNode
            .toList().flatten()
            .findAll { node -> !node.isFile && node.size <= 100000 }
            .collect({ node -> node.size })
            .sum()
}


static Integer partTwo(Node rootNode) {
    def necessarySpace = rootNode.size - 40000000

    return Collections.min(
        rootNode
            .toList().flatten()
            .findAll { node -> !node.isFile && node.size >= necessarySpace }
            .collect({ node -> node.size })
    )
}

static void main(String[] args) {
    def rootNode = readInput()

    println partOne(rootNode)
    println partTwo(rootNode)
}
