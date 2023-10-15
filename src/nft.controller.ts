import { Controller, Post, Body } from '@nestjs/common';
import { exec } from 'child_process';
import { ConfigService } from '@nestjs/config';  // Make sure to import ConfigService

@Controller('nft')
export class NFTController {
  constructor(private configService: ConfigService) { }

  @Post('run')
  async runNFTTool(@Body() data: any): Promise<any> {
    const openaiApiKey = this.configService.get<string>('OPENAI_API_KEY');
    console.log("Received data:", data);
    console.log("OpenAI API Key:", openaiApiKey);

    return new Promise((resolve, reject) => {
      // Include the API key in the command if needed
      const pythonProcess = exec(`python ./services/nft_tool.py ${data.topic} ${data.industry1} ${data.industry2} ${data.exclusion1} ${data.exclusion2} ${data.date_start} ${data.date_end} ${openaiApiKey}`);

      let result = '';

      pythonProcess.stdout?.on('data', (data) => {
        result += data.toString();
      });

      pythonProcess.stderr?.on('data', (data) => {
        console.error(`stderr: ${data}`);
      });

      pythonProcess.on('close', (code) => {
        if (code !== 0) {
          console.error(`Python script exited with code ${code}`);
          return reject(new Error(`Python script exited with code ${code}`));
        }
        return resolve(result);
      });
    });
  }
}
