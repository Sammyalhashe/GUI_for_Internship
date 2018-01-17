/*
An LRU Cache is a memory structure that is used for quickly accessing
elements previously referenced in a task. The purpose of this is to speed
procedures up. The 'LRU' is an acronym for 'Least Recently Used'. If the cache is
full, the element that is least recently used is removed in favour of adding a new one


Implmentation:
1) Two data structures are used to implement a common LRU cache:
    a) A hash table to represent the stored values in the cache
    b) Doubly Linked-List to represent the position of each item in the cache
*/

import java.util.*;

public class lruCache {

    /* class vars */
    private HashMap < Integer, Node > map;
    private LinkedList LL;

    /* private variable declarations */
    private int _cacheSize;

    /* Constructor for the cache */
    public lruCache(int cacheSize) {
        this.setCacheSize(cacheSize);
        map = new HashMap < Integer, Node > ();
        LL = this.new LinkedList();
    }

    /* Getters and Setters for the instance variables */

    public int getCacheSize() {
        return this._cacheSize;
    }

    public void setCacheSize(int cacheSize) throws IllegalArgumentException {
        if (cacheSize <= 0) {
            throw new IllegalArgumentException("Size of the cache must be greater than 0");
        } else {
            this._cacheSize = cacheSize;
        }
    }

    /* Inner class Node for the doubly linked list */

    class Node {
        int key;
        int value;
        Node pre = null;
        Node next = null;

        Node(int key, int value) {
            this.key = key;
            this.value = value;
        }

    }

    private class LinkedList {

        // Head + Tail for LL
        public Node head;
        public Node tail;


        LinkedList() {
            head = null;
            tail = null;
        }


        /* add to head and remove methods */

        public void addHead(Node n) {
            if (this.head == null && this.tail == null) {
                this.head = n;
                this.tail = n;
            } else {
                n.next = this.head;
                this.head.pre = n;
                this.head = n;
            }
        }

        public void removeNode(Node n) throws IllegalArgumentException {
            if (this.head == null && this.tail == null) {
                if (n.pre != null) {
                    n.pre.next = n.next;
                } else {
                    this.head = n.next;
                }

                if (n.next != null) {
                    n.next.pre = n.pre;
                } else {
                    this.tail = n.pre;
                }
            } else {
                throw new IllegalArgumentException("LinkedList is empty!");
            }
        }
    }

    /* methods for adding/removing from cache */
    public int getVal(int key) {
        if (this.map.containsKey(key)) {
            Node n = this.map.get(key);
            this.LL.removeNode(n);
            this.LL.addHead(n);
            return n.value;
        } else {
            return -1;
        }
    }

    public void setVal(int key, int value) {
        if (this.map.containsKey(key)) {
            Node old = this.map.get(key);
            this.LL.removeNode(old);
            old.value = value;
            this.LL.addHead(old);
        } else {
            Node created = new Node(key, value);
            if (map.size() >= getCacheSize()) {
                Node nodeRemove = this.LL.tail;
                // remove from the HashMap
                this.map.remove(nodeRemove.key);
                // remove from the LinkedList
                this.LL.removeNode(nodeRemove);
                this.LL.addHead(created);
            } else {
                this.LL.addHead(created);
            }
            this.map.put(key, created);
        }
    }
}