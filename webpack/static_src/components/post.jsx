import React, { Component } from 'react';
import { Panel, Row } from 'react-bootstrap';
import Avatar from 'material-ui/Avatar';

class PostComponent extends Component {
    state = {
        user: {
            id: 0,
            username: '',
        },
        date: '',
        text: '',
    };

    componentDidMount() {
        this.setState({
            date: this.props.date,
            text: this.props.text,
        });

        fetch(this.props.author,
            {
                method: 'GET',
                credentials: 'same-origin',
            })
            .then(promise => promise.json())
            .then((json) => {
                this.setState({
                    user: json,
                });
            });
    }

    render() {
        return (
            <div>
                <Row>
                    <Panel
                        footer={this.state.date}
                        bsStyle="info"
                    >
                        {this.state.text}
                    </Panel>
                </Row>
            </div>
        )
    }
}

PostComponent.propTypes = {
    author: React.PropTypes.string.isRequired,
    date: React.PropTypes.string.isRequired,
    text: React.PropTypes.string.isRequired,
};

export default PostComponent;