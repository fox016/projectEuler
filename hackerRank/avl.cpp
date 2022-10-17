/* Node is defined as :
typedef struct node
{
    int val;
    struct node* left;
    struct node* right;
    int ht;
} node; */

node* insert(node* root, int val);
bool insertHelper(node*& curnode, int val);
int getBalance(node* n);
void rebalance(node*& n);
void rotateRight(node*& n);
void rotateLeft(node*& n);
void updateHeight(node* n);
void preorderPrint(node* n);
void postorderUpdateHeight(node* n);

node* insert(node* root, int val)
{
    postorderUpdateHeight(root);
    insertHelper(root, val);
    postorderUpdateHeight(root);
    return root;
}

bool insertHelper(node*& curnode, int val)
{
    if(curnode == NULL) {
        node* newNode = new node();
        newNode->val = val;
        newNode->ht = 0;
        curnode = newNode;
        return true;
    }
    else if (val < curnode->val) {
        bool isAdded = insertHelper(curnode->left, val);
        rebalance(curnode);
        return isAdded;
    }
    else if (val > curnode->val) {
        bool isAdded = insertHelper(curnode->right, val);
        rebalance(curnode);
        return isAdded;
    }
    else if (val == curnode->val) {
        cout << "Duplicate value: " << val << endl;
        return false;
    }
    cout << "Why here? Why now?" << endl;
    return false;
}

void rebalance(node*& n)
{
    if(n == NULL)
        return;
    cout << "Rebalance " << n->val << endl;
    int balance = getBalance(n);
    cout << "balance " << n->val << ": " << balance << endl;
    if(balance == 2)
    {
        int leftBalance = getBalance(n->left);
        if(leftBalance == 1 || leftBalance == 0)
        {
            rotateRight(n);
        }
        else if(leftBalance == -1)
        {
            rotateLeft(n->left);
            rotateRight(n);
        }
        else {
            cout << "Invalid left balance " << n->left->val << ": " << leftBalance << endl;
        }
    }
    else if(balance == -2)
    {
        int rightBalance = getBalance(n->right);
        if(rightBalance == 1)
        {
            rotateRight(n->right);
            rotateLeft(n);
        }
        else if(rightBalance == -1 || rightBalance == 0)
        {
            rotateLeft(n);
        }
        else {
            cout << "Invalid right balance " << n->right->val << ": " << rightBalance << endl;
        }
    }
    postorderUpdateHeight(n);
}

int getBalance(node* n)
{
    if(n == NULL)
        return 0;
    postorderUpdateHeight(n);
    if(n->left == NULL && n->right == NULL)
        return 0;
    if(n->left == NULL)
        return -1 - n->right->ht;
    if(n->right == NULL)
        return n->left->ht + 1;
    return n->left->ht = n->right->ht;
}

void rotateRight(node*& n)
{
    cout << "rotate right " << n->val << endl;
    node* temp = n;
    n = n->left;
    temp->left = n->right;
    n->right = temp;
    postorderUpdateHeight(n);
}

void rotateLeft(node*& n)
{
    cout << "rotate left " << n->val << endl;
    node* temp = n;
    n = n->right;
    temp->right = n->left;
    n->left = temp;
    postorderUpdateHeight(n);
}

void updateHeight(node* n)
{
    if(n == NULL)
        return;
    if(n->left == NULL && n->right == NULL)
        n->ht = 0;
    else if(n->left == NULL)
        n->ht = n->right->ht + 1;
    else if(n->right == NULL)
        n->ht = n->left->ht + 1;
    else {
        int lHt = n->left->ht;
        int rHt = n->right->ht;
        if(lHt > rHt)
            n->ht = lHt+1;
        else
            n->ht = rHt + 1;
    }
}

void preorderPrint(node* n)
{
    if(n == NULL)
        return;
    cout << "node " << n->val << ": " << n->ht << endl;
    preorderPrint(n->left);
    preorderPrint(n->right);
}

void postorderUpdateHeight(node* n)
{
    if(n == NULL)
        return;
    postorderUpdateHeight(n->left);
    postorderUpdateHeight(n->right);
    updateHeight(n);
}
