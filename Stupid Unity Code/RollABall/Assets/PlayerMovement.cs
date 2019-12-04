using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    private Rigidbody m_Rigidbody;

    public bool breakWall;

    public float speed;
    private float scrollSpeed;
    public float zSpeed;

    public static bool hudActive = false;

    private static bool freeze = false;

    private const float dirChange = 2.0f / 3.0f;

    // Start is called before the first frame update
    void Start()
    {
        m_Rigidbody = GetComponent<Rigidbody>();
        Physics.gravity = new Vector3(0, -30.0F, 0);
        scrollSpeed = speed;

    }


    bool IsGrounded(){
       return Physics.Raycast(transform.position, -Vector3.up, GetComponent<Collider>().bounds.extents.y + 0.1f);
     }

// Update is called once per frame
void Update()
    {
        if (hudActive)
        {
            m_Rigidbody.useGravity = false;
            m_Rigidbody.velocity = new Vector3(0, 0, 0);
        }
        else
        {
            m_Rigidbody.useGravity = true;
        }
        if (freeze) return;
        if (transform.position.y <= -10)
        {
            HazardImpact.deathReset(this.gameObject);
        }
        if (!IsGrounded()) return;
        if (Input.GetKey(KeyCode.LeftArrow) || Input.GetKey(KeyCode.A))
        {
            //Move the Rigidbody backwards constantly at the speed you define (the blue arrow axis in Scene view)
            m_Rigidbody.velocity = new Vector3(scrollSpeed, 0, zSpeed);

        }
        if (Input.GetKey(KeyCode.RightArrow) || Input.GetKey(KeyCode.D))
        {
            m_Rigidbody.velocity = new Vector3(scrollSpeed, 0, -zSpeed);

        }
        m_Rigidbody.velocity = new Vector3(scrollSpeed, 0, m_Rigidbody.velocity.z);

    }

    public static void freezeGame(bool state)
    {
        freeze = state;
    }

    public void resetSpeed()
    {
        scrollSpeed = speed;
    }

    public void setScrollSpeed(float speed)
    {
        scrollSpeed = speed;
    }

    public float getScrollSpeed()
    {
        return scrollSpeed;
    }

    
}
