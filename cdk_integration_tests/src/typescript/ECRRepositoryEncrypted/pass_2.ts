import * as cdk from 'aws-cdk-lib';
import * as ecr from 'aws-cdk-lib/aws-ecr';
import {Construct} from 'constructs';

export class exampleStack extends cdk.Stack {
    constructor(scope: Construct, id: string, props?: cdk.StackProps) {
        super(scope, id, props);
        const repository = new ecr.Repository(this, 'Repo', {
            encryptionKey: new kms.Key(this, 'Key')
        });
    }
}

const app = new cdk.App();
new exampleStack(app, 'example-stack');
app.synth();
