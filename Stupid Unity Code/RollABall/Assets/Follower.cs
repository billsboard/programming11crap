using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Follower : MonoBehaviour
{
    // Start is called before the first frame update

    GameObject go;
    Rigidbody rb;

    public static int zCor;

    void Start()
    {
        go = GameObject.Find("Player");
        rb = go.GetComponentInChildren<Rigidbody>();
    }

    // Update is called once per frame
    void Update()
    {
        transform.position = new Vector3(rb.position.x, rb.position.y, zCor);
    }
}
