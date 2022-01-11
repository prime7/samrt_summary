import React, { useState } from 'react'
import axios from 'axios'
import { SUMMARY_POST, SUMMARY_RATE_POST } from './API';


export default function Summary() {
    const [step,setStep] = useState(0);
    const [link,setLink] = useState("");
    const [content,setContent] = useState("");
    const [summary,setSummary] = useState("");
    const [id,setId] = useState();

    const submit = () => {
        const config = {
            headers: {
                'Content-Type': 'application/json',
            },
        };
        let body;
        if (link.length>1){
            body = JSON.stringify({
                src_link:  link,
            });
        }
        else{
            body = JSON.stringify({
                content: content
            });
        }
        axios
        .post(SUMMARY_POST, body, config)
        .then((res) => {
            setStep(1)
            setSummary(res.data.summary)
            setId(res.data.id)
        })
        .catch((err) => {
            console.error(err)
        });

    }
    const renderForm = () => {
        switch(step){
            case 0:
                return <InputSummary link={link} setLink={setLink} content={content} setContent={setContent} submit={submit}/>
            case 1:
                return <ShowSummary summary={summary} id={id}/>
            default:
                return <h1>Something went wrong</h1>
        }
    }

    return (
        <div className="container-fluid">
            {renderForm()}
        </div>
    )
}


const InputSummary = ({link, setLink, content, setContent, submit}) => {
    return(
        <>
            <div className="row">
                <input 
                    type="url" 
                    placeholder="Wikipedia page link" 
                    name="homepage" 
                    className="w-50 mx-auto mt-5" 
                    style={{lineHeight:"3em"}}
                    onChange={e=> setLink(e.target.value)}
                    value={link}
                />
            </div>
            <div className="row">
                <textarea 
                    className="w-50 mx-auto mt-2" 
                    rows="20" 
                    placeholder="Or paste content here to get summary"
                    onChange={e=>setContent(e.target.value)}
                    value={content}
                />
            </div>
            <div className="row">
                <button 
                    type="button" 
                    className="btn btn-outline-success w-25 mx-auto mt-2"
                    onClick={submit}
                >
                    Get Summary
                </button>
            </div>
        </>
    )
}

const ShowSummary = ({summary,id}) => {
    const [show,setShow] = useState(true)
    const loggedIn = localStorage.getItem('smrtsmry-user')
    const submitRating = (e) => {
        const config = {
            headers: {
                'Content-Type': 'application/json',
            },
        };
        const body = JSON.stringify({
            summary_id : id,
            rate : e.target.value
        })

        axios
        .post(SUMMARY_RATE_POST, body, config)
        .then((res) => {
            setShow(false)
        })
        .catch((err) => {
            console.error(err)
        });
    }
    return (
        <div className="row m-5">
            <div className="jumbotron jumbotron">
                <h1 className="display-4">Summary</h1>
                <p className="lead">
                    {summary}
                </p>
            </div>
            {loggedIn && show &&  (
                <div className="row justify-content-center mt-5">
                <div className="col-md-3">
                <div className="card p-2 text-dark bg-light">
                    <div className="card-header">Rate Summary</div>
                    <div className="form-check">
                        <input className="form-check-input" type="radio" name="rating" value={0} onChange={submitRating}/> ★
                    </div>
                    <div className="form-check">
                        <input className="form-check-input" type="radio" name="rating" value={1} onChange={submitRating}/> ★★
                    </div>
                    <div className="form-check">
                        <input className="form-check-input" type="radio" name="rating" value={2} onChange={submitRating}/> ★★★
                    </div>
                </div>
                </div>
                </div>
            )}
            {!show && (
                <div className="alert alert-success" role="alert">
                    Thanks for the feedback!
                </div>
            )}
        </div>
    )
}